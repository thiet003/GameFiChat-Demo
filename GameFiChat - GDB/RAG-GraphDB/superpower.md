CREATE
(countsRatingSuperpowerSquad:COUNTSRATING{
    ratings: 575, 
    starRating: 4, 
    counts1star: 2, 
    counts2star: 5, 
    counts3star: 2, 
    counts4star: 12, 
    counts5star: 554 
}),
(countsLikeSuperpowerSquad:COUNTSLIKES{
    like: 634, 
    dislike: 0
}),
(socialscoreSuperpowerSquad:SOCIALSCORE{
    timeframe: "24h",
    socialScore: 68.78607177734375,
    telegramGroupScore: 87.46261596679688,
    telegramChannelScore: 2.8039159774780273,
    twitterScore: 53.599998474121094,
    discordScore: 0,
    socialRank: 242,
    telegramGroup_rank: 70,
    telegramChannelRank: 230,
    twitterRank: 274,
    discordRank: 372
}),
(communityPerformanceSuperpowerSquad:COMMUNITYPERFORMANCE{
    telegramGroupUsers: 15716,
    twitterFollowers: 93494,
    twitterInteraction: 2,
    communityRank: "A",
    marketRank: 42.36706689536878,
    twitterRank: "B",
    telegramGroupRank: "S"
}),
(staffsSuperpowerSquad1:STAFFS{
    name: "Greg Gopman",
    position: "CEO",
    description: "",
    link: "https://www.linkedin.com/in/gregorygopman"
}),
(staffsSuperpowerSquad2:STAFFS{
    name: "Pony Zhang",
    position: "CTO"
}),
(teamProfileSuperpowerSquad:TEAMPROFILE{
    name: "Superpower Squad",
    teamRank: "C"
}),
(teamProfileSuperpowerSquad)-[:HAVE_STAFF]-> (staffsSuperpowerSquad1),
(teamProfileSuperpowerSquad)-[:HAVE_STAFF]-> (staffsSuperpowerSquad2),

(topBackersSuperpowerSquad1:TOPBACKERS{
    name: "Ankr",
    linkWebsite: "https://www.ankr.com/"
}),
(teamProfileLikeSuperpowerSquad:TEAMPROFILELIKE{
    likes: 100,
    dislikes: 0,
    like_changed: 100
}),
(SuperpowerSquadGame:GAMES{
    id: 4,
    name: "superpower-squad",
    about: "INTRODUCTION \n Superpower Squad is a blockchain technology-based third-person-shooter game consists of gameplays such as MOBA, RPG, and Roguelike. The game supports solo and team modes, with immersive gaming experience, diverse game mode, and delicate hero & skin & weapon synthesis and upgrade system. Superpower Squad is going to bring eSports culture to web3 for all players. The mobile app has integrated a native in-app wallet to lower down the learning cost of web2 gamers. With innovative gaming model and user-friendly blockchain infrastructure, Superpower Squad will lead the eSports in web3 industry."
}),
(SuperpowerSquadGame)-[:HAVE_NUMBER_LIKES]-> (countsLikeSuperpowerSquad),
(SuperpowerSquadGame)-[:HAVE_NUMBER_RATES]-> (countsRatingSuperpowerSquad),
(SuperpowerSquadGame)-[:HAVE_SOCIAL_SCORE]-> (socialscoreSuperpowerSquad),
(SuperpowerSquadGame)-[:HAVE_COMMUNITY_PERFORMANCE]-> (communityPerformanceSuperpowerSquad),
(SuperpowerSquadGame)-[:HAVE_TEAM]-> (teamProfileSuperpowerSquad),
(SuperpowerSquadGame)-[:HAVE_TOP_BACKERS]-> (topBackersSuperpowerSquad1),
(SuperpowerSquadGame)-[:HAVE_TEAM_PROFILE_LIKES]-> (teamProfileLikeSuperpowerSquad)