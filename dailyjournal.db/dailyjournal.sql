CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`subject`	TEXT NOT NULL,
	`date`	TEXT NOT NULL,
    `timespent`	TEXT NOT NULL,
    `moods_id` INTEGER NOT NULL,
    FOREIGN KEY(`moods_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);

INSERT INTO `Entries` VALUES (null, "Functions", "1/2/2022", 1, 1);
INSERT INTO `Entries` VALUES (null, "For Loops", "1/12/2022", 3, 2);
INSERT INTO `Entries` VALUES (null, ".Maps", "1/15/2022", 2, 2);
INSERT INTO `Entries` VALUES (null, "REACT", "1/18/2022", 5 , 3);
INSERT INTO `Entries` VALUES (null, "Fetch Calls", "1/23/2022", 5, 3);


INSERT INTO `Moods` VALUES (null, "excited");
INSERT INTO `Moods` VALUES (null, "eager");
INSERT INTO `Moods` VALUES (null, "nervous");