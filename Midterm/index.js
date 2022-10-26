
RESOURCES = ["wool", "grain", "lumber", "brick", "ore"]

const generate_player = () => {
    return {
        "wool": 0,
        "grain": 0,
        "lumber": 0,
        "brick": 0,
        "ore": 0,
        points: 0
    };
};

const exchange_at = () => {return 3}

const discard_at = () => {return 7}

const get_random_resource = () => {
    return RESOURCES[Math.floor(5 * Math.random())]
}

const receive_res = (player, res_name, converter) => {
    player[res_name] += 1
    if (player[res_name] == converter())
    {
        player.points += 1
        player[res_name] = 0
    }
    return player
};


const get_total_resources = (player) => {
    let total = 0
    for (const res of RESOURCES)
        total += player[res]
    return total
}

const discard = (player) => {
    for (const res of RESOURCES)
        player[res] = Math.floor(player[res] / 2)
    return player
}

const is_winner = (player) => {
    if (player.points === 10)
        return true
    else
        return false
}


const runGame = () => {

    let players = new Array(10).fill(null).map(() => generate_player())
    
    let round = 1;
    let gameOver = false
    console.log("*** GAME STARTS ***")
    console.log("============================================================")
    while (!gameOver)
    {
        console.log(`Round ${round}: ---------------------------------------------------`)
        for (let i = 0; i < 10; i++)
        {
            players[i] = receive_res(players[i], get_random_resource(), exchange_at)
            console.log(`Player ${i} has  ${players[i]["wool"]} wool, ${players[i]["grain"]} grain, ${players[i]["lumber"]} lumber, ${players[i]["brick"]} brick, and ${players[i]["ore"]} ore.`)
            console.log(`Points for player ${i}: ${players[i].points}`)
            // console.log(get_total_resources(players[i]))
            if (is_winner(players[i]))
            {
                console.log(`Player ${i} won the game`)
                gameOver = true
                break
            }
            if (get_total_resources(players[i]) === discard_at())
            {
                players[i] = discard(players[i]);
                console.log(`Player ${i} must discard!`)
                console.log(`They now have ${players[i]["wool"]} wool, ${players[i]["grain"]} grain, ${players[i]["lumber"]} lumber, ${players[i]["brick"]} brick, and ${players[i]["ore"]} ore.`)
            }
        }
        round++;
    }
    console.log("============================================================")
    console.log("*** GAME IS OVER ***")
}

runGame();
