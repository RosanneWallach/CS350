// FP code that allows companies to pay employees

const generate_player = (name, race, gender, hitpoints) => {
    return {
        name: name,
        race: race,
        gender: gender,
        team: "",
        hitpoints: hitpoints
    };
};

const generate_monster = (name, race, gender, hitpoints) => {
    return {
        name: name,
        race: race,
        gender: gender,
        hitpoints: hitpoints
    };
};

const take_hitpoints = (actor, hp) => {
    return Object.assign(
        {},
        actor,
        {
            hitpoints: actor.hitpoints - hp
        }
    );
};


const simulation = () => {
    p_1 = generate_player("Player-1", "P", "M", 20);
    m_1 = generate_monster("Monster-1", "M", "F", 35);

    console.log('Starting ...');
    let round = 1;
    while(p_1.hitpoints > 0 && m_1.hitpoints > 0)
    {
        console.log(`Round ${round}: --------------------------`);
        console.log(`${p_1.name}: ${p_1.hitpoints}`);
        console.log(`${m_1.name}: ${m_1.hitpoints}`);
        m_1 = take_hitpoints(m_1, 1);
        p_1 = take_hitpoints(p_1, 2);
        round += 1;
    }
    console.log(`END ================================`);
    console.log(`${p_1.name}: ${p_1.hitpoints}`);
    console.log(`${m_1.name}: ${m_1.hitpoints}`);
};

simulation();
