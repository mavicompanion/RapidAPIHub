import json

# Assuming `data` is your JSON content loaded from the `data.json` file
data = '''
{
    "meta": {
        "version": "v1.0",
        "status": 200,
        "copywrite": "https://apicalls.io",
        "symbol": "AAPL",
        "processedTime": "2024-09-28T18:35:35.646517Z",
        "modules": "earnings"
    },
    "body": {
        "earnings": {
            "maxAge": 86400,
            "earningsChart": {
                "quarterly": [
                    {"date": "2Q2024", "actual": {"raw": 1.4, "fmt": "1.40"}, "estimate": {"raw": 1.35, "fmt": "1.35"}},
                    {"date": "4Q2023", "actual": {"raw": 2.18, "fmt": "2.18"}, "estimate": {"raw": 2.1, "fmt": "2.10"}},
                    {"date": "1Q2024", "actual": {"raw": 1.53, "fmt": "1.53"}, "estimate": {"raw": 1.5, "fmt": "1.50"}},
                    {"date": "3Q2023", "actual": {"raw": 1.36, "fmt": "1.36"}, "estimate": {"raw": 1.3, "fmt": "1.30"}}
                ],
                "currentQuarterEstimate": {"raw": 1.6, "fmt": "1.60"},
                "currentQuarterEstimateDate": "4Q",
                "currentQuarterEstimateYear": 2023,
                "earningsDate": [
                    {"raw": 1730372340, "fmt": "2024-10-31"},
                    {"raw": 1730721600, "fmt": "2024-11-04"}
                ],
                "isEarningsDateEstimate": true
            },
            "financialsChart": {
                "yearly": [
                    {"date": 2020, "revenue": {"raw": 274515000000, "fmt": "274.51B", "longFmt": "274,515,000,000"}, "earnings": {"raw": 57411000000, "fmt": "57.41B", "longFmt": "57,411,000,000"}},
                    {"date": 2021, "revenue": {"raw": 365817000000, "fmt": "365.82B", "longFmt": "365,817,000,000"}, "earnings": {"raw": 94680000000, "fmt": "94.68B", "longFmt": "94,680,000,000"}},
                    {"date": 2022, "revenue": {"raw": 394328000000, "fmt": "394.33B", "longFmt": "394,328,000,000"}, "earnings": {"raw": 99803000000, "fmt": "99.8B", "longFmt": "99,803,000,000"}}
                ]
            }
        }
    }
}
'''

if __name__ == "__main__":

    # Parse the JSON data
    parsed_data = json.loads(data)

    # Access meta information
    version = parsed_data['meta']['version']
    symbol = parsed_data['meta']['symbol']

    # Access quarterly earnings information
    quarterly_earnings = parsed_data['body']['earnings']['earningsChart']['quarterly']

    for q in quarterly_earnings:
        date = q['date']
        actual_earnings = q['actual']['raw']
        estimated_earnings = q['estimate']['raw']
        print(f"Date: {date}, Actual: {actual_earnings}, Estimate: {estimated_earnings}")

    # Access current quarter estimate
    current_estimate = parsed_data['body']['earnings']['earningsChart']['currentQuarterEstimate']['raw']
    print(f"Current Quarter Estimate: {current_estimate}")

    # Access yearly financials
    yearly_financials = parsed_data['body']['earnings']['financialsChart']['yearly']

    for year in yearly_financials:
        date = year['date']
        revenue = year['revenue']['raw']
        earnings = year['earnings']['raw']
        print(f"Year: {date}, Revenue: {revenue}, Earnings: {earnings}")
