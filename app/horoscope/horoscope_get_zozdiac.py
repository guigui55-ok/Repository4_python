from datetime import date

class ZodiacNumbers:
    ARIES = 1               # おひつじ座
    TAURUS = 2              # おうし座
    GEMINI = 3              # ふたご座
    CANCER = 4              # かに座
    LEO = 5                 # しし座
    VIRGO = 6               # おとめ座
    LIBRA = 7               # てんびん座
    SCORPIO = 8             # さそり座
    SAGITTARIUS = 9         # いて座
    CAPRICORN = 10          # やぎ座
    AQUARIUS = 11           # みずがめ座
    PISCES = 12             # うお座

class ZodiacSignsJP:
    SIGNS = {
        ZodiacNumbers.ARIES: "おひつじ座",
        ZodiacNumbers.TAURUS: "おうし座",
        ZodiacNumbers.GEMINI: "ふたご座",
        ZodiacNumbers.CANCER: "かに座",
        ZodiacNumbers.LEO: "しし座",
        ZodiacNumbers.VIRGO: "おとめ座",
        ZodiacNumbers.LIBRA: "てんびん座",
        ZodiacNumbers.SCORPIO: "さそり座",
        ZodiacNumbers.SAGITTARIUS: "いて座",
        ZodiacNumbers.CAPRICORN: "やぎ座",
        ZodiacNumbers.AQUARIUS: "みずがめ座",
        ZodiacNumbers.PISCES: "うお座",
    }

def get_zodiac_name_from_number(number: int) -> str:
    """
    星座番号から星座名を取得する関数。

    :param number: 星座番号 (int)
    :return: 星座名 (str)
    """
    return ZodiacSignsJP.SIGNS.get(number, "不明な星座")

def get_zodiac_number(birth_date: date) -> str:
    """
    指定された日付に基づいて星座名を返す。

    :param birth_date: 誕生日 (datetime.date)
    :return: 星座名 (str)
    """
    month = birth_date.month
    day = birth_date.day
    zodiac_number = None

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_number = ZodiacNumbers.ARIES
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_number = ZodiacNumbers.TAURUS
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_number = ZodiacNumbers.GEMINI
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_number = ZodiacNumbers.CANCER
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_number = ZodiacNumbers.LEO
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_number = ZodiacNumbers.VIRGO
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_number = ZodiacNumbers.LIBRA
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_number = ZodiacNumbers.SCORPIO
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_number = ZodiacNumbers.SAGITTARIUS
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_number = ZodiacNumbers.CAPRICORN
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_number = ZodiacNumbers.AQUARIUS
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_number = ZodiacNumbers.PISCES

    return zodiac_number

# 使用例
if __name__ == "__main__":
    print(" \n****** ")
    birth_date = date(1995, 6, 15)  # 例: 1995年6月15日

    zodiac_number = get_zodiac_number(birth_date)
    print(f"誕生日 {birth_date} の星座番号は {zodiac_number} です。")
    # 番号から星座名を取得する
    zodiac_name = get_zodiac_name_from_number(zodiac_number)
    print(f"番号 {zodiac_number} の星座は {zodiac_name} です。")
