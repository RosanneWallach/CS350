/**
 * Generates a player object with the given params
 * @param {*} name Player's name
 * @param {*} race Player's race
 * @param {*} gender Player's gender
 * @param {*} hitpoints Player's intial hitpoints
 * @returns player object
 */
const generate_player = (name, race, gender, hitpoints) => {
    return {
        name: name,
        race: race,
        gender: gender,
        team: "",
        hitpoints: hitpoints
    };
};

/**
 * Generates a monster object with given arguments
 * @param {*} name Monster's name
 * @param {*} race Monster's race
 * @param {*} gender Monster's gender
 * @param {*} hitpoints Monster's initial hitpoints
 * @returns monster object
 */
const generate_monster = (name, race, gender, hitpoints) => {
    return {
        name: name,
        race: race,
        gender: gender,
        hitpoints: hitpoints
    };
};


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
            hitpoints: actor.hitpoints - hp
        }
    );
};


/**
 * Simulates DND game as described in instructions
 */
const simulation = () => {
    // Creating player and monster objects
    p_1 = generate_player("Player-1", "P", "M", 20);
    m_1 = generate_monster("Monster-1", "M", "F", 35);

    console.log('Starting ...');
    let round = 1;
    // Running undefined number of rounds until game is over
    while(p_1.hitpoints > 0 && m_1.hitpoints > 0)
    {
        // Displaying round state
        console.log(`Round ${round}: --------------------------`);
        console.log(`${p_1.name}: ${p_1.hitpoints}`);
        console.log(`${m_1.name}: ${m_1.hitpoints}`);
        // Takes hitpoints from both sides and move on to next round
        m_1 = take_hitpoints(m_1, 1);
        p_1 = take_hitpoints(p_1, 2);
        round += 1;
    }
    // Displaying results
    console.log(`END ================================`);
    console.log(`${p_1.name}: ${p_1.hitpoints}`);
    console.log(`${m_1.name}: ${m_1.hitpoints}`);
};

simulation();
