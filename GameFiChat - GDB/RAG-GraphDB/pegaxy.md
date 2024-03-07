CREATE
(countsRatingPEGAXY:COUNTSRATING{
    ratings: 2, 
    starRating: 4, 
    counts1star: 0, 
    counts2star: 0, 
    counts3star: 0, 
    counts4star: 2, 
    counts5star: 0 
}),
(countsLikePEGAXY:COUNTSLIKES{
    like: 27, 
    dislike: 0
}),
(socialscorePEGAXY:SOCIALSCORE{
    timeframe: "24h",
    socialScore: 86.59369659423828,
    telegramGroupScore: 0,
    telegramChannel_score: 94.6383056640625,
    twitterScore: 74.30496978759766,
    discordScore:96.65157318115234,
    socialRank: 100,
    telegramGroup_rank: 487,
    telegramChannelRank: 32,
    twitterRank: 196,
    discordRank: 19
}),
(communityPerformancePEGAXY:COMMUNITYPERFORMANCE{
    twitterFollowers: 82025,
    discordUsers: 92365,
    twitterInteraction: 19,
    telegramInteraction: 4,
    discordInteraction: 7927,
    communityRank: "S",
    marketRank: 23.842195540308747,
    twitterRank: "A",
    discordRank: "S"
}),
(staffsPEGAXY1:STAFFS{
    name: "Vu Nguyen Van",
    position: "CTO",
    description: "",
    link: "https://www.linkedin.com/in/vunv518/"
}),
(staffsPEGAXY2:STAFFS{
    name: "Corey Wilton",
    position: "CEO",
    link: "https://www.linkedin.com/in/realcoreywilton/",
    description: ""
}),
(teamProfilePEGAXY:TEAMPROFILE{
    name: "Mirai Labs",
    teamRank: "b"
}),
(teamProfilePEGAXY)-[:HAVE_STAFF]-> (staffsPEGAXY1),
(teamProfilePEGAXY)-[:HAVE_STAFF]-> (staffsPEGAXY2),

(topBackersPEGAXY1:TOPBACKERS{
    name: "Kyber Ventures",
    linkWebsite: "https://www.kyber.ventures/"
}),
(topBackersPEGAXY2:TOPBACKERS{
    name: "Shima Capital",
    linkWebsite: "https://shima.capital/"
}),
(topBackersPEGAXY3:TOPBACKERS{
    name: "TK Ventures",
    linkWebsite: "https://tk.ventures/"
}),
(topBackersPEGAXY4:TOPBACKERS{
    name: "Poolz Ventures",
    linkWebsite: "https://ventures.poolz.finance/"
}),
(topBackersPEGAXY5:TOPBACKERS{
    name: "Kyros Ventures",
    linkWebsite: "https://kyros.ventures/"
}),
(topBackersPEGAXY6:TOPBACKERS{
    name: "Kyber Network",
    linkWebsite: "https://kyber.network/"
}),
(teamProfileLikePEGAXY:TEAMPROFILELIKE{
    likes: 100,
    dislikes: 0,
    like_changed: 100
}),
(PEGAXYGame:GAMES{
    id: 2,
    name: "pegaxy",
    backerRank: "S",
    about: "INTRODUCTION \n Pegaxy is a play-to-earn PVP style horse racing game where players compete for top 3 placement against 14 other racers. Each race has randomised elemental variables which include wind, water, fire, speed and more. Using strategic upgrades, food and skill, players must place in the top 3 to earn the platforms utility token, VIS (Vigorus). \n Within the game, players are able to breed, merge, rent, sell, and of course race their Pega to earn VIS tokens. This system has proven to be a sound long-term economic approach when building an NFT/Blockchain based game as it enables teams to build large guilds, scholarship programs, and even provides solo players the opportunity to earn in game tokens through daily racing. \n The initial sale of 5,000 Founding Pega was held in October 2021, alongside the PGX launch via IDO in November. The first 5,000 Pega were dubbed \"Founding\" Pega as they were the only ones  created by the Pegaxy Development team. Every Pega after #5,000 has been minted (created) through the breeding model inside the game. \n Pegaxy is well respected within the industry for its innovation in trustless rental systems, on chain technology and well weighted economic balance. Many also attribute its popularity to the gameplay, team transparency and community involvement during the development process.",
    play_mode: "{\"time\":1668501651472,\"blocks\":[{\"id\":\"k8WomETC83\",\"type\":\"paragraph\",\"data\":{\"text\":\"Pegaxy has a very unique ecosystem that allows players to enter any race, for free. With this economic model, gameplay is very competitive, however the rewards are still lucrative. Players compete against 14 other racers in an attempt to earn a top 3 placement. All players inside the top 3 earn VIS tokens, the platforms utility token. Knowledge, strategy and skill are all required to place in the top 3. Be prepared to race, dedicate time and be one with your Pega, the rewards will make it all worthwhile.\"}}],\"version\":\"2.23.2\"}",
    play_to_earn_model: "{\"time\":1668501588978,\"blocks\":[{\"id\":\"2s7lSkD_Zj\",\"type\":\"paragraph\",\"data\":{\"text\":\"Owners and Renters can earn by:\"}},{\"id\":\"IWQlaqSYDA\",\"type\":\"list\",\"data\":{\"style\":\"unordered\",\"items\":[\"Racing their Pega in PVP mode.\",\"Selling high performing or newly born Pega on the Marketplace.\",\"Renting-out their Pega in the Rental Marketplace for a share of racing profit or fixed term rental.\",\"Collecting rare \\\"Founding\\\" and \\\"Crowned\\\" Pega and reselling through marketplace price speculation.\",\"Competing in Pegaxy's global competition, \\\"The Grand Dash\\\". This competition takes place over 12 months, concluding in December, in which the top 12 racers of every class (60 total/month), compete in a series of events until the top 15 racers are identified at the Grand final in December (top 3 of each class). The top 15 will receive generous PGX rewards.\"]}}],\"version\":\"2.23.2\"}"
}),
(PEGAXYGame)-[:HAVE_NUMBER_LIKES]-> (countsLikePEGAXY),
(PEGAXYGame)-[:HAVE_NUMBER_RATES]-> (countsRatingPEGAXY),
(PEGAXYGame)-[:HAVE_SOCIAL_SCORE]-> (socialscorePEGAXY),
(PEGAXYGame)-[:HAVE_COMMUNITY_PERFORMANCE]-> (communityPerformancePEGAXY),
(PEGAXYGame)-[:HAVE_TEAM]-> (teamProfilePEGAXY),
(PEGAXYGame)-[:HAVE_TOP_BACKERS]-> (topBackersPEGAXY1),
(PEGAXYGame)-[:HAVE_TOP_BACKERS]-> (topBackersPEGAXY2),
(PEGAXYGame)-[:HAVE_TOP_BACKERS]-> (topBackersPEGAXY3),
(PEGAXYGame)-[:HAVE_TOP_BACKERS]-> (topBackersPEGAXY4),
(PEGAXYGame)-[:HAVE_TOP_BACKERS]-> (topBackersPEGAXY5),
(PEGAXYGame)-[:HAVE_TOP_BACKERS]-> (topBackersPEGAXY6),
(PEGAXYGame)-[:HAVE_TEAM_PROFILE_LIKES]-> (teamProfileLikePEGAXY)

