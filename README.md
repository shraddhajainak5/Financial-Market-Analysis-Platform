# Financial Market Analysis Platform

A full-stack web application for searching and analyzing stock information using the Finnhub Stock API and Polygon.io API.

## Live Demo

[View Live Demo](https://shraddhaassignment2stock.wl.r.appspot.com)

## Features

- **Stock Search**: Search for any publicly listed company using their ticker symbol
- **Company Information**: View company profiles including logo, exchange information, and industry category
- **Stock Summary**: Display real-time stock data with price changes and trading metrics
- **Interactive Charts**: Visualize historical stock prices and trading volume using HighCharts
- **Recommendation Trends**: See current buy/sell recommendations from market analysts
- **Latest News**: Browse recent financial news articles related to the searched company

## Project Structure

```
StockSense/
│
├── static/                 # Static files
│   ├── back.svg            # Background SVG for main page
│   ├── search-solid.svg    # Search icon
│   ├── times-solid.svg     # Clear button icon
│   ├── style.css           # Main stylesheet
│   ├── GreenArrowUp.png    # Up arrow for positive changes
│   └── RedArrowDown.png    # Down arrow for negative changes
│
├── templates/              # HTML templates (if using templates)
│   └── index.html          # Main HTML file
│
├── backend.py              # Flask backend server
├── requirements.txt        # Python dependencies
├── app.yaml                # App Engine configuration (for GCP deployment)
└── README.md               # Project documentation
```

## Technology Stack

### Frontend
- HTML5, CSS3, JavaScript
- HighCharts for interactive data visualization

### Backend
- Python with Flask framework
- RESTful API architecture

### APIs
- Finnhub Stock API for company information, stock quotes, and news
- Polygon.io API for historical market data
- HighCharts API for data visualization

### Deployment
- Deployed on Google Cloud App Engine/AWS/Azure

## Data Flow

1. User enters a stock ticker symbol
2. Backend Flask server processes the request
3. Server makes API calls to Finnhub and Polygon.io
4. Data is processed and returned to the frontend
5. Frontend renders the data in appropriate formats (tables, charts, etc.)

## Implementation Details

### Backend

The server-side implementation uses Flask to create endpoints that proxy requests to financial APIs:

- `/displaythecontent`: Fetches company profile information
- `/newscontent`: Retrieves latest news articles
- `/summarycontent`: Gets current stock price summary
- `/recommendationcontent`: Obtains analyst recommendations
- `/chartcontent`: Retrieves historical data for chart visualization

### Frontend

The frontend features a responsive design with a tab-based navigation system:

- **Company Tab**: Displays company logo and business information
- **Stock Summary Tab**: Shows current stock prices and market indicators
- **Charts Tab**: Interactive visualization of price history with selectable timeframes
- **Latest News Tab**: Recent news related to the company with direct links to articles

## API Documentation

### Finnhub API
- Company Profile: `https://finnhub.io/api/v1/stock/profile2`
- Stock Quotes: `https://finnhub.io/api/v1/quote`
- Company News: `https://finnhub.io/api/v1/company-news`
- Recommendations: `https://finnhub.io/api/v1/stock/recommendation`

### Polygon.io API
- Aggregate Bars: `https://api.polygon.io/v2/aggs/ticker/{stockTicker}/range/{multiplier}/{timespan}/{from}/{to}`

## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Requests module
- dateutil module

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StockSense.git
   cd StockSense
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API keys:
   ```
   FINNHUB_API_KEY=your_finnhub_api_key
   POLYGON_API_KEY=your_polygon_api_key
   ```

4. Run the application:
   ```bash
   python backend.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Testing

Test the application with various stock tickers such as:
- AAPL (Apple)
- MSFT (Microsoft)
- TSLA (Tesla)
- AMZN (Amazon)
- GOOGL (Google)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Finnhub](https://finnhub.io/) for providing financial data API
- [Polygon.io](https://polygon.io/) for historical stock data
- [HighCharts](https://www.highcharts.com/) for interactive data visualization
- [Flask](https://flask.palletsprojects.com/) for the web framework
