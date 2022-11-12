const NAMES_P = ["Kyl", "Den", "Phi", "Adm", "Ana"]
const NAMES_M = ["Fox", "Lio", "Snk", "Wlf", "Egl"]


/**
 * Generates a random integer between 0 and max excluded.
 * @param {*} max 
 * @returns random int
 */
const rand_int_max = (max) => {
    return Math.floor(Math.random() * max);
}


/**
 * Generates a random integer between 0 and max excluded.
 * @param {*} max 
 * @returns random int
 */
const rand_int_range = (min, max) => {
    return min + Math.floor(Math.random() * (max - min));
}


/**
 * Generates a player object with the given params
 * @param {*} name Player's name
 * @param {*} race Player's race
 * @param {*} hitpoints Player's intial hitpoints
 * @returns player object
 */
const generate_player = (name, hitpoints, dmg_level) => {
    return {
        name: name,
        hitpoints: hitpoints,
        damage_level: dmg_level
    };
};


/**
 * Generates a player with random values
 * @returns player object
 */
const player_randomizer = () => {
    name_p = NAMES_P[rand_int_max(NAMES_P.length)]
    hitpoints = rand_int_range(10, 21)
    damage_level = rand_int_range(1, 4)
    return generate_player(name_p, hitpoints, damage_level);
}


/**
 * Generates a monster object with given arguments
 * @param {*} name Monster's name
 * @param {*} race Monster's race
 * @param {*} gender Monster's gender
 * @param {*} hitpoints Monster's initial hitpoints
 * @returns monster object
 */
const generate_monster = (name, hitpoints, dmg_level) => {
    return {
        name: name,
        hitpoints: hitpoints,
        damage_level: dmg_level
    };
};


/**
 * Generates a monster with random values
 * @returns monster object
 */
const monster_randomizer = () => {
    name_m = NAMES_M[rand_int_max(NAMES_M.length)]
    hitpoints = rand_int_range(20, 31)
    damage_level = rand_int_range(2, 5)
    return generate_monster(name_m, hitpoints, damage_level);
}


/**
 * Generates a game state with a monster and 3 random players
 * @returns Game state object
 */
const generate_game_state = () => {
    return {
        players: Array(3).fill(null).map(player_randomizer),
        monsters: Array(1).fill(null).map(monster_randomizer),
        round: 0,
    }
}


/**
 * Takes a specific number of hitpoints from the given player/monster
 * @param {*} actor player/monster object
 * @param {*} hp hitpoints to be taken
 * @returns updated object
 */
const take_hitpoints = (actor, hp) => {
    return Object.assign(
        {},
        actor,
        {
            hitpoints: actor.hitpoints - hp < 0 ? 0 : actor.hitpoints - hp
        }
    );
};


/**
 * A helper function to sum up damage level of team members
 * @param {*} a previous value
 * @param {*} b next value
 * @returns 
 */
const sum_damage = (a, b) => {
    return a + b.damage_level
}


/**
 * Plays players turn
 * @param {*} gs Game state object
 * @returns Updated game state object
 */
const players_round = (gs) => {
    damage = gs.players.reduce(sum_damage, 0)
    return {
        ...gs,
        monsters: gs.monsters.map(m => take_hitpoints(m, damage))
    }
}


/**
 * Plays monster turn
 * @param {*} gs Game state object
 * @returns Updated game state object
 */
const monster_round = (gs) => {
    // Picking a random primary player
    rp = rand_int_max(gs.players.length)
    dmg = gs.monsters[0].damage_level
    return {
        ...gs,
        players: gs.players.map((p, i) => take_hitpoints(p, rp == i ? 2 * damage : damage))
    }
}


/**
 * Checks if a player/monster is alive (hitpoints > 0)
 * @param {*} actor player/monster object
 * @returns True if alive, False otherwise
 */
const is_alive = (actor) => {
    return actor.hitpoints > 0;
}


/**
 * Cleaning the game state by removing dead members
 * @param {*} gs Game state object
 * @returns Updated game state object
 */
const cleanup = (gs) => {
    return {
        ...gs,
        players: gs.players.filter(is_alive),
        monsters: gs.monsters.filter(is_alive)
    }
}


/**
 * Plays a single round by running 1 round for each side
 * @param {*} gs Game state object
 * @returns Updated game state object
 */
const play_round = (gs) => {
    gs.round = gs.round + 1
    gs = players_round(gs)
    gs = monster_round(gs)
    gs = cleanup(gs)
    return gs
}


/**
 * Displays the current game state
 * @param {*} gs Game state object
 */
const announce = (gs) => {
    console.log(`Round ${gs.round}: --------------------------`);
    gs.players.map(print_player)
    gs.monsters.map(print_monster)
}



/**
 * Print player/monster info on the console log
 * @param {*} actor player/monster object
 */
const print_player = (actor) => {
    console.log(`Player (${actor.name}: ${actor.hitpoints})`);
}


/**
 * Print player/monster info on the console log
 * @param {*} actor player/monster object
 */
const print_monster = (actor) => {
    console.log(`Monster [${actor.name}: ${actor.hitpoints}]`);
}


/**
 * Checks if a game is over or not
 * @param {*} gs 
 * @returns 
 */
const is_game_over = (gs) => {
    return gs.players.length === 0 || gs.monsters.length === 0;
}


/**
 * Simulates DND game as described in instructions
 */
const simulation = () => {

    game_state = generate_game_state()
    console.log(game_state)
    announce(game_state)
    console.log('Starting ...');
    while(!is_game_over(game_state))
    {
        // Displaying round state
        game_state = play_round(game_state)
        announce(game_state)
    }
    console.log(`END ================================`);
};

simulation();
