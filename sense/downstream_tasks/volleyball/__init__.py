LAB2INT_CLASSIFICATION = {
    "Holding Ball": 0,
    "Forearm Passing": 1,
    "Pokey": 2,
    "Dropping Ball": 3,
    "Doing Nothing": 4,
    "Bouncing Ball": 5,
    "One Arm Passing": 6,
    "Leaving Screen": 7,
    "Overhead Passing": 8
}

LAB2INT_COUNTING = {
    "background": 0,
    "holding_ball_position_1": 1,
    "holding_ball_position_2": 2,
    "forearm_passing_position_1": 3,
    "forearm_passing_position_2": 4,
    "pokey_position_1": 5,
    "pokey_position_2": 6,
    "dropping_ball_position_1": 7,
    "dropping_ball_position_2": 8,
    "doing_nothing_position_1": 9,
    "doing_nothing_position_2": 10,
    "bouncing_ball_position_1": 11,
    "bouncing_ball_position_2": 12,
    "one_arm_passing_position_1": 13,
    "one_arm_passing_position_2": 14,
    "leaving_screen_position_1": 15,
    "leaving_screen_position_2": 16,
    "overhead_passing_position_1": 17,
    "overhead_passing_position_2": 18
}

INT2LAB_CLASSIFICATION = {value: key for key, value in LAB2INT_CLASSIFICATION.items()}
INT2LAB_COUNTING = {value: key for key, value in LAB2INT_COUNTING.items()}

CLASSIFICATION_THRESHOLDS = {
    "Holding Ball": 0.4,
    "Forearm Passing": 0.6,
    "Pokey": 0.85,
    "Dropping Ball": 0.6,
    "Doing Nothing": 0.4,
    "Bouncing Ball": 0.6,
    "One Arm Passing": 0.6,
    "Leaving Screen": 0.8,
    "Overhead Passing": 0.6
}
