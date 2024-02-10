

from typing import List, Tuple
from datetime import datetime


def parse_line(line: str,card_number) -> Tuple[datetime, int, str, int]:
    """
    Parse a line of input and return a tuple containing:
    - The datetime of the event
    - The card number
    - The type of event (AUTH or CAPTURE)
    - The amount of the event
    """
    # "[2020-11-01 23:58] Card #98 AUTH 100",
    # "[2020-11-02 00:40] Capture 50",

    parts = line.split()
    timestamp = datetime.strptime((parts[0] + " " + parts[1]).strip('[]'), '%Y-%m-%d %H:%M')
    if len(parts) > 4: # card

        card_number = int(parts[3].strip('#'))
        event_type = 'auth'
        amount = int(parts[5])
    else: # capture

        event_type = 'capture'
        amount = int(parts[3])

    return timestamp, card_number, event_type, amount


def most_morning_captures(lines: List[str]) -> Tuple[int, int]:
    """
    Find the card with the most captures in non-active times (2200-2359 and 0000-0759).
    """
    card_number = -1
    capture_counts = {}
    for line in lines:
        timestamp, card_number, event_type, amount = parse_line(line,card_number)
        # print(timestamp, card_number, event_type, amount)
        if event_type.upper() == 'CAPTURE' and (0 <= timestamp.hour < 8 or 22 <= timestamp.hour < 24) and amount >0:
            capture_counts[card_number] = capture_counts.get(card_number, 0) + 1

    if not capture_counts:
        return (-1, -1)

    max_captures_card = max(capture_counts, key=capture_counts.get)
    return (max_captures_card, capture_counts[max_captures_card])


def most_overcaptured_amount(lines: List[str]) -> Tuple[int, int]:
    """
    For the card that has the largest captured amount, sum amounts from positive capture events.
    """
    capture_amounts = {}
    authLimit = {}
    card_number = -1
    for line in lines:
        timestamp, card_number, event_type, amount = parse_line(line,card_number)
        if event_type.upper() == 'AUTH':
            capture_amounts[card_number]= [0,amount]
        if event_type.upper() == 'CAPTURE' and amount > 0 and card_number in capture_amounts:
            capture_amounts[card_number][0] +=  amount

    # for card in capture_amounts:
    #
    #     if card in authLimit and capture_amounts[card] > authLimit[card]:
    #         capture_amounts[card] = authLimit[card]
    for k,v in capture_amounts.items():
        if v[0] > v[1]:
            print('overriden',v[0],v[1])
            capture_amounts[k] = v[1]

    if not capture_amounts:
        return (-1, -1)

    max_amount_card = max(capture_amounts, key=capture_amounts.get)
    return (max_amount_card, capture_amounts[max_amount_card][0])


def most_negative_captures(lines: List[str]) -> Tuple[int, int]:
    """
    Find the card that has the most negative captures.
    """
    negative_capture_counts = {}
    card_number = -1
    for line in lines:
        timestamp, card_number, event_type, amount = parse_line(line,card_number)
        if event_type.upper() == 'CAPTURE' and amount < 0:
            negative_capture_counts[card_number] = negative_capture_counts.get(card_number, 0) + 1

    if not negative_capture_counts:
        return (-1, -1)


    max_negative_captures_card = max(negative_capture_counts, key=negative_capture_counts.get)
    return (max_negative_captures_card, negative_capture_counts[max_negative_captures_card])


#
# lines = [
#     "[2020-11-01 23:58] Card #98 AUTH 100",
#     "[2020-11-02 00:40] Capture 50",
#     "[2020-11-03 00:05] CARD #17 AUTH 100",
#     "[2020-11-03 00:24] Capture 50",
#     "[2020-11-05 00:03] Card #90 AUTH 200",
#     "[2020-11-05 00:45] CAPTURE 34",
#     "[2020-11-01 00:00] Card #10 AUTH 300",
#     "[2020-11-01 00:05] CAPTURE 300",
#     "[2020-11-01 00:30] CAPTURE 200",
#     "[2020-11-04 00:02] Card #97 AUTH 400",
#     "[2020-11-04 00:36] CAPTURE 30"
# ]


lines  = ['[2020-05-09 09:40] CAPTURE 39', '[2020-05-06 14:11] CAPTURE 10', '[2020-05-14 13:27] CAPTURE -4', '[2020-05-14 08:30] CAPTURE -21', '[2020-05-08 01:34] CAPTURE 1', '[2020-05-08 15:34] CAPTURE -3', '[2020-05-12 21:42] Card #42 AUTH 891', '[2020-05-10 14:07] CAPTURE -35', '[2020-05-08 04:04] Card #16 AUTH 985', '[2020-05-08 22:01] CAPTURE -35', '[2020-05-08 12:42] CAPTURE -49', '[2020-05-11 09:09] CAPTURE 50', '[2020-05-14 05:27] CAPTURE 39', '[2020-05-13 05:43] Card #43 AUTH 306', '[2020-05-12 22:59] CAPTURE -18', '[2020-05-08 01:19] CAPTURE 20', '[2020-05-14 02:13] CAPTURE 7', '[2020-05-13 22:32] CAPTURE 15', '[2020-05-10 20:35] Card #30 AUTH 558', '[2020-05-11 04:27] CAPTURE -14', '[2020-05-13 03:45] CAPTURE -28', '[2020-05-09 23:45] CAPTURE 47', '[2020-05-08 06:58] CAPTURE 25', '[2020-05-09 20:37] Card #25 AUTH 398', '[2020-05-06 07:48] CAPTURE 29', '[2020-05-12 09:14] CAPTURE 47', '[2020-05-10 22:10] CAPTURE -7', '[2020-05-13 07:12] CAPTURE -47', '[2020-05-11 04:25] CAPTURE -21', '[2020-05-13 12:36] CAPTURE -12', '[2020-05-10 15:21] Card #29 AUTH 569', '[2020-05-08 19:52] CAPTURE 18', '[2020-05-06 01:36] Card #6 AUTH 660', '[2020-05-06 07:39] Card #8 AUTH 66', '[2020-05-12 00:41] Card #38 AUTH 893', '[2020-05-09 06:27] CAPTURE 30', '[2020-05-05 17:58] CAPTURE 4', '[2020-05-12 14:23] CAPTURE -47', '[2020-05-08 12:52] Card #18 AUTH 837', '[2020-05-14 10:52] Card #49 AUTH 326', '[2020-05-09 05:04] CAPTURE 28', '[2020-05-08 11:02] CAPTURE 25', '[2020-05-10 11:17] CAPTURE 17', '[2020-05-08 08:32] Card #17 AUTH 515', '[2020-05-09 11:45] CAPTURE 44', '[2020-05-06 17:28] CAPTURE 14', '[2020-05-10 23:20] CAPTURE -7', '[2020-05-10 06:52] Card #27 AUTH 655', '[2020-05-13 15:09] Card #45 AUTH 471', '[2020-05-06 19:44] CAPTURE 31', '[2020-05-08 18:57] Card #19 AUTH 580', '[2020-05-11 16:53] Card #36 AUTH 879', '[2020-05-11 19:27] CAPTURE 20', '[2020-05-05 11:03] CAPTURE -12', '[2020-05-13 20:53] CAPTURE -37', '[2020-05-13 11:13] CAPTURE -7', '[2020-05-10 11:00] CAPTURE -11', '[2020-05-11 01:59] CAPTURE -6', '[2020-05-09 09:40] CAPTURE -47', '[2020-05-12 16:48] CAPTURE 10', '[2020-05-13 23:25] Card #46 AUTH 482', '[2020-05-07 15:42] Card #14 AUTH 400', '[2020-05-05 20:16] CAPTURE 13', '[2020-05-08 19:59] CAPTURE -37', '[2020-05-09 01:27] CAPTURE -27', '[2020-05-07 22:20] Card #15 AUTH 898', '[2020-05-06 03:31] CAPTURE -37', '[2020-05-09 23:57] CAPTURE 0', '[2020-05-11 06:16] CAPTURE -10', '[2020-05-10 09:17] CAPTURE 22', '[2020-05-10 19:51] CAPTURE 8', '[2020-05-11 22:56] CAPTURE 32', '[2020-05-10 05:36] CAPTURE 33', '[2020-05-08 22:32] Card #21 AUTH 809', '[2020-05-05 10:49] Card #2 AUTH 590', '[2020-05-09 14:42] CAPTURE 23', '[2020-05-07 20:03] CAPTURE -19', '[2020-05-07 14:39] CAPTURE -40', '[2020-05-11 05:06] Card #32 AUTH 827', '[2020-05-14 07:52] CAPTURE 4', '[2020-05-11 13:34] CAPTURE 45', '[2020-05-06 12:59] CAPTURE 5', '[2020-05-10 21:04] CAPTURE -8', '[2020-05-05 09:01] CAPTURE 24', '[2020-05-12 19:09] CAPTURE -35', '[2020-05-14 00:52] CAPTURE 28', '[2020-05-14 03:37] Card #47 AUTH 739', '[2020-05-14 15:23] CAPTURE 32', '[2020-05-06 10:34] Card #9 AUTH 365', '[2020-05-11 15:17] CAPTURE 10', '[2020-05-07 02:21] CAPTURE -17', '[2020-05-08 16:10] CAPTURE 9', '[2020-05-05 14:26] Card #3 AUTH 375', '[2020-05-05 19:10] Card #4 AUTH 101', '[2020-05-14 08:04] Card #48 AUTH 308', '[2020-05-11 10:51] Card #34 AUTH 74', '[2020-05-05 15:49] CAPTURE -49', '[2020-05-07 11:10] CAPTURE -22', '[2020-05-06 13:08] CAPTURE 31', '[2020-05-09 07:45] Card #23 AUTH 340', '[2020-05-08 06:38] CAPTURE 41', '[2020-05-05 22:22] Card #5 AUTH 784', '[2020-05-10 02:43] CAPTURE 12', '[2020-05-11 17:08] CAPTURE -50', '[2020-05-11 20:53] Card #37 AUTH 765', '[2020-05-07 07:23] Card #12 AUTH 842', '[2020-05-07 10:34] CAPTURE -41', '[2020-05-08 03:03] CAPTURE -14', '[2020-05-05 08:16] CAPTURE 33', '[2020-05-10 12:10] Card #28 AUTH 847', '[2020-05-06 04:27] Card #7 AUTH 291', '[2020-05-07 16:41] CAPTURE 17', '[2020-05-05 13:20] CAPTURE -47', '[2020-05-07 17:08] CAPTURE 37', '[2020-05-13 12:14] Card #44 AUTH 727', '[2020-05-06 14:42] Card #10 AUTH 520', '[2020-05-10 14:29] CAPTURE -42', '[2020-05-07 04:23] CAPTURE 50', '[2020-05-13 10:04] CAPTURE 49', '[2020-05-11 01:12] Card #31 AUTH 307', '[2020-05-10 00:35] Card #26 AUTH 952', '[2020-05-09 15:49] CAPTURE -49', '[2020-05-09 18:45] CAPTURE -9', '[2020-05-10 17:07] CAPTURE -19', '[2020-05-07 00:11] CAPTURE -28', '[2020-05-12 01:55] CAPTURE 19', '[2020-05-06 02:22] CAPTURE -34', '[2020-05-12 03:24] CAPTURE -4', '[2020-05-13 01:13] CAPTURE -23', '[2020-05-12 11:47] Card #40 AUTH 987', '[2020-05-12 04:49] CAPTURE -36', '[2020-05-08 23:25] CAPTURE -43', '[2020-05-12 06:35] CAPTURE -3', '[2020-05-05 23:36] CAPTURE -26', '[2020-05-12 03:41] Card #39 AUTH 704', '[2020-05-07 09:23] CAPTURE 4', '[2020-05-05 05:19] Card #1 AUTH 852', '[2020-05-07 13:18] Card #13 AUTH 94', '[2020-05-11 08:19] Card #33 AUTH 644', '[2020-05-06 06:54] CAPTURE -6', '[2020-05-13 17:53] CAPTURE -40', '[2020-05-09 04:26] Card #22 AUTH 929', '[2020-05-09 20:46] CAPTURE -1', '[2020-05-06 22:13] Card #11 AUTH 295', '[2020-05-09 13:42] Card #24 AUTH 652']

print(most_morning_captures(lines))
print(most_overcaptured_amount(lines))
print(most_negative_captures(lines))
print(len(lines))