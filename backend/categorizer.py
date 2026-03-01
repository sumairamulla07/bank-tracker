def categorize_merchant(merchant_name):
    if not merchant_name:
        return "Other"

    merchant = merchant_name.lower().strip()

    categories = {
        "Food": [
            "zomato", "swiggy", "dominos", "mcdonalds", "kfc", "subway",
            "pizzahut", "burgerking", "dunkin", "starbucks", "chaayos",
            "faasos", "box8", "freshmenu", "eatsure"
        ],
        "Grocery": [
            "bigbasket", "blinkit", "grofers", "jiomart", "dmart",
            "zepto", "swiggyinstamart", "dunzo", "milkbasket", "nature"
        ],
        "Shopping": [
            "amazon", "flipkart", "myntra", "ajio", "meesho", "nykaa",
            "snapdeal", "tatacliq", "reliance", "shopsy", "mamaearth"
        ],
        "Travel": [
            "irctc", "rapido", "ola", "uber", "redbus", "makemytrip",
            "goibibo", "yatra", "cleartrip", "airasia", "indigo",
            "spicejet", "olacabs", "meru"
        ],
        "Entertainment": [
            "netflix", "spotify", "hotstar", "primevideo", "youtube",
            "bookmyshow", "pvr", "inox", "zee5", "sonyliv", "jiosaavn",
            "gaana", "wynk"
        ],
        "Bills": [
            "electricity", "airtel", "jio", "vodafone", "bsnl", "tata",
            "bescom", "mseb", "adani", "torrent", "paytm", "phonepe",
            "gpay", "billdesk"
        ],
        "Health": [
            "pharmeasy", "netmeds", "1mg", "apollo", "medplus",
            "practo", "docprime", "healthkart", "cult", "fitpass"
        ],
        "Education": [
            "byju", "unacademy", "vedantu", "coursera", "udemy",
            "whitehat", "toppr", "doubtnut", "classplus"
        ]
    }

    # Check if merchant matches any category
    for category, merchants in categories.items():
        if any(m in merchant for m in merchants):
            return category

    return "Other"