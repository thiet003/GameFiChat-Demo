CREATE
(countsRatingGodsUchained:COUNTSRATING{
    ratings: 11, 
    starRating: 4, 
    counts1star: 0, 
    counts2star: 1, 
    counts3star: 0, 
    counts4star: 4, 
    counts5star: 6 
}),
(countsLikeGodsUchained:COUNTSLIKES{
    like: 975, 
    dislike: 0
}),
(socialscoreGodsUchained:SOCIALSCORE{
    timeframe: "24h",
    socialScore: 47.57627487182617,
    telegramGroupScore: 0,
    telegramChannel_score: 0,
    twitterScore: 80.77539825439453,
    discordScore: 0,
    socialRank: 412,
    telegramGroup_rank: 445,
    telegramChannelRank: 471,
    twitterRank: 136,
    discordRank: 580
}),
(communityPerformanceGodsUchained:COMMUNITYPERFORMANCE{
    twitterFollowers: 128754,
    twitterInteraction: 74,
    communityRank: "S",
    marketRank: 12.178387650085764,
    twitterRank: "S"
}),
(staffsGodsUchained1:STAFFS{
    link: "https://www.linkedin.com/in/matt-aldrich-6b78241/",
    name: "Matt Aldrich",
    position: "Lead Art Director",
    description: "Matt Aldrich has extensive experience Art Directing games in Europe, America, and Asia, and has been focused on delivering world class game art for multiple triple-A titles for over 20 years. His experience includes studios such as EA, Lucasfilm, and Wargaming where he worked on games spanning console, PC, and mobile. Throughout his career, Aldrich has worked on industry leading franchises including Tomb Raider, Assassins Creed, James Bond, Lord of the Rings, FIFA, and Star Wars."
}),
(staffsGodsUchained2:STAFFS{
    link: "https://www.linkedin.com/in/arashmahboubi/",
    name: "Arash Mahboubi",
    position: "Crypto Product Lead",
    description: "Arash brings with him a deep understanding of the crypto ecosystem and blockchain development. He’s been building the core technology that governs the Ethereum network for over 4 years and previous to that helped bring blockchain Dapps (Decentralized applications) to mainstream consumers. As a passionate gamer he brings together his technical expertise to overcome the technical divide between crypto concepts and traditional game mechanisms that players have grown to learn and love."
}),
(staffsGodsUchained3:STAFFS{
    name: "Derek Proud",
    position: "Producer",
    description: "Derek Proud is a games industry veteran with more than 20 years experience. He’s worked on many licensed titles such as Harry Potter, Avatar: The Last Airbender, Cars, Spongebob Squarepants, and Jimmy Neutron as well as a variety of unlicensed franchises such as Destroy All Humans!, EA Sports Cricket, and EA Sports Rugby. He was both designer and producer for Big Beach Sports on Wii, which sold more than 2 million units worldwide."
}),
(teamProfileGodsUchained:TEAMPROFILE{
    name: "Immutable",
    teamRank: "S"
}),
(teamProfileGodsUchained)-[:HAVE_STAFF]-> (staffsGodsUchained1),
(teamProfileGodsUchained)-[:HAVE_STAFF]-> (staffsGodsUchained2),
(teamProfileGodsUchained)-[:HAVE_STAFF]-> (staffsGodsUchained3),

(topBackersGodsUchained1:TOPBACKERS{
    name: "Galaxy",
    linkWebsite: "https://www.galaxydigital.io/"
}),
(topBackersGodsUchained2:TOPBACKERS{
    name: "Coinbase Ventures",
    linkWebsite: "https://www.coinbase.com/ventures"
}),
(topBackersGodsUchained3:TOPBACKERS{
    name: "Bitkraft Ventures",
    linkWebsite: "https://www.bitkraft.vc/"
}),
(topBackersGodsUchained4:TOPBACKERS{
    name: "Fabric Ventures",
    linkWebsite: "https://www.fabric.vc/"
}),
(topBackersGodsUchained5:TOPBACKERS{
    name: "Continue Capital",
    linkWebsite: "https://continue.capital/"
}),
(topBackersGodsUchained6:TOPBACKERS{
    name: "OKX Ventures",
    linkWebsite: "https://www.okx.com/blockdream-ventures"
}),
(topBackersGodsUchained7:TOPBACKERS{
    name: "Alameda Research",
    linkWebsite: "https://www.alameda-research.com/"
}),
(teamProfileLikeGodsUchained:TEAMPROFILELIKE{
    likes: 100,
    dislikes: 0,
    like_changed: 100
}),
(GodsUchainedGame:GAMES{
    id: 5,
    name: "gods-unchained",
    backerRank: "S",
    about: "INTRODUCTION \n Superpower Squad is a blockchain technology-based third-person-shooter game consists of gameplays such as MOBA, RPG, and Roguelike. The game supports solo and team modes, with immersive gaming experience, diverse game mode, and delicate hero & skin & weapon synthesis and upgrade system. Superpower Squad is going to bring eSports culture to web3 for all players. The mobile app has integrated a native in-app wallet to lower down the learning cost of web2 gamers. With innovative gaming model and user-friendly blockchain infrastructure, Superpower Squad will lead the eSports in web3 industry.",
    play_to_earn_model: "{\"time\":1655712343013,\"blocks\":[{\"id\":\"-oxb0FgY_w\",\"type\":\"paragraph\",\"data\":{\"text\":\"170,000,000 $GODS tokens (34% of total) are reserved for the Play to Earn Rewards pool. This is the largest allocation as Play to Earn is the key value proposition of Gods Unchained. With this rewards pool, we aim to attract a large group of active players to participate in the Gods Unchained ecosystem. A fixed amount of $GODS tokens will be allocated to a variety of Play to Earn campaigns such as:\"}},{\"id\":\"pB-5Gc8vxR\",\"type\":\"paragraph\",\"data\":{\"text\":\"Weekend Ranked reward\"}},{\"id\":\"Ukdg89hF_2\",\"type\":\"paragraph\",\"data\":{\"text\":\"Daily token reward system\"}},{\"id\":\"TV5pbmOZHL\",\"type\":\"paragraph\",\"data\":{\"text\":\"Quest\"}},{\"id\":\"mW4GiYA-ev\",\"type\":\"paragraph\",\"data\":{\"text\":\"Seasonal reward\"}},{\"id\":\"1slVaSu7zC\",\"type\":\"paragraph\",\"data\":{\"text\":\"Tournament\"}},{\"id\":\"7YtyaT0vLd\",\"type\":\"paragraph\",\"data\":{\"text\":\"Special game modes\"}}],\"version\":\"2.23.2\"}"
}),
(GodsUchainedGame)-[:HAVE_NUMBER_LIKES]-> (countsLikeGodsUchained),
(GodsUchainedGame)-[:HAVE_NUMBER_RATES]-> (countsRatingGodsUchained),
(GodsUchainedGame)-[:HAVE_SOCIAL_SCORE]-> (socialscoreGodsUchained),
(GodsUchainedGame)-[:HAVE_COMMUNITY_PERFORMANCE]-> (communityPerformanceGodsUchained),
(GodsUchainedGame)-[:HAVE_TEAM]-> (teamProfileGodsUchained),
(GodsUchainedGame)-[:HAVE_TOP_BACKERS]-> (topBackersGodsUchained1),
(GodsUchainedGame)-[:HAVE_TOP_BACKERS]-> (topBackersGodsUchained2),
(GodsUchainedGame)-[:HAVE_TOP_BACKERS]-> (topBackersGodsUchained3),
(GodsUchainedGame)-[:HAVE_TOP_BACKERS]-> (topBackersGodsUchained4),
(GodsUchainedGame)-[:HAVE_TOP_BACKERS]-> (topBackersGodsUchained5),
(GodsUchainedGame)-[:HAVE_TOP_BACKERS]-> (topBackersGodsUchained6),
(GodsUchainedGame)-[:HAVE_TOP_BACKERS]-> (topBackersGodsUchained7),
(GodsUchainedGame)-[:HAVE_TEAM_PROFILE_LIKES]-> (teamProfileLikeGodsUchained)

