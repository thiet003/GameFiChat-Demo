CREATE
(countsRatingGunstarMetaverse:COUNTSRATING{
    ratings: 2, 
    starRating: 4, 
    counts1star: 2, 
    counts2star: 0, 
    counts3star: 0, 
    counts4star: 2, 
    counts5star: 6155 
}),
(countsLikeGunstarMetaverse:COUNTSLIKES{
    like: 10635, 
    dislike: 0
}),
(socialscoreGunstarMetaverse:SOCIALSCORE{
    timeframe: "24h",
    socialScore: 77.6964340209961,
    telegramGroupScore: 29.683147430419922,
    telegramChannel_score: 3.7240495681762695,
    twitterScore: 52.98304748535156,
    discordScore: 82.80806732177734,
    socialRank: 171,
    telegramGroup_rank: 218,
    telegramChannelRank: 82,
    twitterRank: 276,
    discordRank: 129
}),
(communityPerformanceGunstarMetaverse:COMMUNITYPERFORMANCE{
    telegramGroupUsers: 12922,
    twitterFollowers: 136050,
    discordUsers: 60364,
    twitterInteraction: 2,
    communityRank: "B",
    marketRank: 49.57118353344768,
    twitterRank: "B",
    telegramGroup_rank: "C",
    discordRank: "S"
}),
(staffsGunstarMetaverse1:STAFFS{
    name: "Hoang Hiep",
    position: "CEO",
    description: "",
    link: "https://www.linkedin.com/in/hoanghiepgunstar/"
}),
(staffsGunstarMetaverse2:STAFFS{
    name: "Tuan Diep",
    position: "CTO",
    link: "https://www.linkedin.com/in/dieptrantuan88",
    description: ""
}),
(staffsGunstarMetaverse3:STAFFS{
    name: "Minh Nhat",
    position: "CMO",
    link: "https://www.linkedin.com/in/minh-nhat-9701b4146/",
    description: ""
}),
(teamProfileGunstarMetaverse:TEAMPROFILE{
    name: "Gunstar Labs",
    teamRank: "A"
}),
(teamProfileGunstarMetaverse)-[:HAVE_STAFF]-> (staffsGunstarMetaverse1),
(teamProfileGunstarMetaverse)-[:HAVE_STAFF]-> (staffsGunstarMetaverse2),
(teamProfileGunstarMetaverse)-[:HAVE_STAFF]-> (staffsGunstarMetaverse3),


(topBackersGunstarMetaverse1:TOPBACKERS{
    name: "DAO Maker",
    linkWebsite: "https://daomaker.com/"
}),
(topBackersGunstarMetaverse2:TOPBACKERS{
    name: "Magnus Capital",
    linkWebsite: "https://shima.capital/https://magnusdigitalassets.com/"
}),
(topBackersGunstarMetaverse3:TOPBACKERS{
    name: "Icetea Labs",
    linkWebsite: "https://icetea.io/#/"
}),
(topBackersGunstarMetaverse4:TOPBACKERS{
    name: "Hashed Fund",
    linkWebsite: "https://www.hashed.com/"
}),
(topBackersGunstarMetaverse5:TOPBACKERS{
    name: "Raptor Capital",
    linkWebsite: "https://www.raptorcapital.io/"
}),
(topBackersGunstarMetaverse6:TOPBACKERS{
    name: "Spark Digital Capital",
    linkWebsite: "https://sparkdigitalcapital.com/"
}),
(teamProfileLikeGunstarMetaverse:TEAMPROFILELIKE{
    likes: 100,
    dislikes: 0,
    like_changed: 100
}),
(GunstarMetaverseGame:GAMES{
    id: 2,
    name: "gunstar-metaverse",
    backerRank: "S",
    about: "INTRODUCTION \n Gunstar Metaverse (Gunstar) is a massively multiplayer online role-playing (RPG) and turn-based strategy NFT Game that gives you the real value of enjoyment and excitement in gaming and the real value provided through the blockchain platform. \n Gunstar is a cyber-prone game for professional gamers or any kinds of users to test their skills and corporate with their correspondents in an attempt to create the ultimate-high shoot, or even have the golden opportunities to engage in so-called whirlwind intellectual games to gain unforgettable victory. \n Gunstar and Fantasy Star World will also imbue players with the experience of reality-based adventures, something that goes beyond what a mere tactic game usually offers. Enthusiasm, thrilling anticipation while playing are core to allure customers interest. \n Let enjoy your shot, your adventure in Star World.",
    play_mode: "{\"time\":1655350087108,\"blocks\":[{\"id\":\"_j5Qlpx-L_\",\"type\":\"paragraph\",\"data\":{\"text\":\"Gunstar is a 2D game that bears the properties of a turn-based and ballistics simulation game. <br><br>In Gunstar, players are placed on 2 opposing teams, the opponent either is an AI monster or a player. They will take turns firing at each other with their pet.<br><br>Each pet has 3 unique skills; 2 normal skill and an Ultimate skill. <br><br>This game also has external factors affected by the result of a match, like terrains condition, winds, and storms. This require players to continuously change their aim and trajectory power while rethinking their strategy at the same time. <br><br>The predictive trajectory system is implemented to assist new players to understand the game quicker, but since it doesn't terrains, winds, and weather conditions, players still need skill, experience and calculation in order to beat the opponent.\"}}],\"version\":\"2.23.2\"}"
}),
(GunstarMetaverseGame)-[:HAVE_NUMBER_LIKES]-> (countsLikeGunstarMetaverse),
(GunstarMetaverseGame)-[:HAVE_NUMBER_RATES]-> (countsRatingGunstarMetaverse),
(GunstarMetaverseGame)-[:HAVE_SOCIAL_SCORE]-> (socialscoreGunstarMetaverse),
(GunstarMetaverseGame)-[:HAVE_COMMUNITY_PERFORMANCE]-> (communityPerformanceGunstarMetaverse),
(GunstarMetaverseGame)-[:HAVE_TEAM]-> (teamProfileGunstarMetaverse),
(GunstarMetaverseGame)-[:HAVE_TOP_BACKERS]-> (topBackersGunstarMetaverse1),
(GunstarMetaverseGame)-[:HAVE_TOP_BACKERS]-> (topBackersGunstarMetaverse2),
(GunstarMetaverseGame)-[:HAVE_TOP_BACKERS]-> (topBackersGunstarMetaverse3),
(GunstarMetaverseGame)-[:HAVE_TOP_BACKERS]-> (topBackersGunstarMetaverse4),
(GunstarMetaverseGame)-[:HAVE_TOP_BACKERS]-> (topBackersGunstarMetaverse5),
(GunstarMetaverseGame)-[:HAVE_TOP_BACKERS]-> (topBackersGunstarMetaverse6),
(GunstarMetaverseGame)-[:HAVE_TEAM_PROFILE_LIKES]-> (teamProfileLikeGunstarMetaverse)
