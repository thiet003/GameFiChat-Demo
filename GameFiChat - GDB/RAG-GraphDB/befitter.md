CREATE
(countsRatingBefitter:COUNTSRATING{
    ratings: 21262, 
    starRating: 4, 
    counts1star: 12, 
    counts2star: 7, 
    counts3star: 15, 
    counts4star: 89, 
    counts5star: 21139
}),
(countsLikeBefitter:COUNTSLIKES{
    like: 12036, 
    dislike: 0
}),
(socialscoreBefitter:SOCIALSCORE{
    timeframe: "24h",
    socialScore: 74,
    telegramGroupScore: 84.26854705810547,
    telegramChannel_score: 3.211449146270752,
    twitterScore: 1.6864051818847656,
    discordScore: 66.58673095703125,
    socialRank: 200,
    telegramGroup_rank: 95,
    telegramChannelRank: 166,
    twitterRank: 426,
    discordRank: 263
}),
(communityPerformanceBefitter:COMMUNITYPERFORMANCE{
    telegramGroupUsers: 11781,
    twitterFollowers: 33072,
    discordUsers: 11644,
    communityRank: "B",
    marketRank: 52.658662092624354,
    twitterRank: "D",
    telegramGroup_rank: "S",
    discordRank: "A"
}),
(staffsBefitter1:STAFFS{
    link: "https://www.linkedin.com/in/banguyenthu/",
    name: "Ba",
    position: "Co-founder",
    description: "Ba has broad experience working on multiple notable blockchain projects, including PolkaFoundry, Red Kite Launchpad, and GameFi.org game hub. Before beFITTER, she is Icetea Labs’ due diligence leader who has evaluated and advised over 30 projects."
}),
(staffsBefitter2:STAFFS{
        name: "Thai Trieu",
        position: " Art-Director",
        description: "He is a professional artist with over 8 years of experience in the gaming industry as a concept artist and illustrator. Thai has a profound knowledge of fiction, films, and games with various themes from several international projects that he has worked on."
}),
(staffsBefitter3:STAFFS{
    name: "Trang Doan",
    position: "Product Owner",
    description: "She has 2.5 years working as a Product Owner, 8 years of experience in software development. She is also a mentor on mentori."
}),
(staffsBefitter4:STAFFS{
    name: "Ha Nguyen",
    position: "Head of Development",
    description: "He has 10 years of experience developing finance and education applications, 1 year working in the blockchain industry. He also has outstanding skills in team management and leadership."
}),
(teamProfileBefitter:TEAMPROFILE{
    name: "Immutable",
    teamRank: "C"
}),
(teamProfileBefitter)-[:HAVE_STAFF]-> (staffsBefitter1),
(teamProfileBefitter)-[:HAVE_STAFF]-> (staffsBefitter2),
(teamProfileBefitter)-[:HAVE_STAFF]-> (staffsBefitter3),
(teamProfileBefitter)-[:HAVE_STAFF]-> (staffsBefitter4),

(topBackersBefitter1:TOPBACKERS{
    name: "Icetea Labs",
    linkWebsite: "https://icetea.io/#/"
}),
(topBackersBefitter2:TOPBACKERS{
    name: "GAINS Associates",
    linkWebsite: "https://www.gains-associates.com/"
}),
(teamProfileLikeBefitter:TEAMPROFILELIKE{
    likes: 100,
    dislikes: 0,
    like_changed: 100
}),
(BefitterGame:GAMES{
    id: 6,
    name: "befitter",
    about: "beFITTER is a web3 fitnessfi and socialfi app that aims to build a healthier ecosystem helping users balance their life, improve mental & physical health, gain achievements and still get monetary incentives.",
    play_mode: "{\"time\":1655799618071,\"blocks\":[{\"id\":\"Kh-6_HBSA7\",\"type\":\"paragraph\",\"data\":{\"text\":\"beFITTER offers a range of game modes to give a player a realistics training experience, including: Solo, With Pet, 1 vs 1 and Tournament.\"}}],\"version\":\"2.23.2\"}",
    play_to_earn_model: "{\"time\":1655799622801,\"blocks\":[{\"id\":\"pQo0pDQuHC\",\"type\":\"paragraph\",\"data\":{\"text\":\"Users need to be equipped with Shoe NFT to get paid (beFITTER token) when they walk/ run/ cycle and join challenge with others. They even can equip NFT Pets as a companion to get more rewards.\"}}],\"version\":\"2.23.2\"}",
    highlight_features: "{\"time\":1655799608934,\"blocks\":[{\"id\":\"HuDS0p761x\",\"type\":\"header\",\"data\":{\"text\":\"Unique Features of beFITTER:\",\"level\":2}},{\"id\":\"FcpHDFwOBt\",\"type\":\"paragraph\",\"data\":{\"text\":\"<b>Shoes NFT:</b>&nbsp;Every sneaker will have different qualities. Users can freely burn tokens to elevate their shoes to a new level and mint new shoes. &nbsp;\"}},{\"id\":\"Rzdg1ic26-\",\"type\":\"paragraph\",\"data\":{\"text\":\"<b>Move &amp; Earn:&nbsp;</b>equipped with NFT shoes, can move outdoors to receive Tokens in beFITTER.\"}},{\"id\":\"0jYQ0o8R-x\",\"type\":\"paragraph\",\"data\":{\"text\":\"<b>Rent feature:</b>\"}},{\"id\":\"j9AbHs0z9s\",\"type\":\"list\",\"data\":{\"style\":\"unordered\",\"items\":[\"Fixed rent:&nbsp;The owner can list his/her digital assets (NFT) on the marketplace together with terms and conditions, including rental duration, listed price,... The renter can then have full access to the asset (the pair of shoes) for the contract duration.\",\"Share profit:&nbsp;Similar to the fixed rent feature, the owner can list his/her digital asset (NFT) on the marketplace and find who wants to borrow them. The revenue earned by using that NFT will be shared between the lender and the borrower (the lender decides the percentages in advance)\"]}},{\"id\":\"OktwqwINiL\",\"type\":\"paragraph\",\"data\":{\"text\":\"<b>In-app NFT marketplace:</b> Users can trade their NFT on the marketplace.\"}},{\"id\":\"DYx1z78Btx\",\"type\":\"paragraph\",\"data\":{\"text\":\"<b>Token swap:</b> Token swap allows users to trade directly between two types of tokens as an atomic transaction; also, users can trade their tokens into stable coins for further purposes.\"}},{\"id\":\"C6A7jESkLF\",\"type\":\"paragraph\",\"data\":{\"text\":\"<b>Decentralized wallet:</b> Decentralized cryptocurrency wallets give you complete control of your digital assets — without platform supervision.\"}}],\"version\":\"2.23.2\"}"
}),
(BefitterGame)-[:HAVE_NUMBER_LIKES]-> (countsLikeBefitter),
(BefitterGame)-[:HAVE_NUMBER_RATES]-> (countsRatingBefitter),
(BefitterGame)-[:HAVE_SOCIAL_SCORE]-> (socialscoreBefitter),
(BefitterGame)-[:HAVE_COMMUNITY_PERFORMANCE]-> (communityPerformanceBefitter),
(BefitterGame)-[:HAVE_TEAM]-> (teamProfileBefitter),
(BefitterGame)-[:HAVE_TOP_BACKERS]-> (topBackersBefitter1),
(BefitterGame)-[:HAVE_TOP_BACKERS]-> (topBackersBefitter2),
(BefitterGame)-[:HAVE_TEAM_PROFILE_LIKES]-> (teamProfileLikeBefitter)

