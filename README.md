# FSx Waste Analyzer

A tool for analyzing AWS FSx for NetApp ONTAP filesystems to identify optimization opportunities and cost-saving recommendations.

## Overview

The FSx Waste Analyzer is a serverless application that helps AWS customers identify potential cost savings and optimization opportunities in their FSx for NetApp ONTAP environments. The tool analyzes filesystem configurations, usage patterns, and performance metrics to provide actionable recommendations.

## Features

- **Comprehensive Analysis**: Evaluates storage efficiency, throughput utilization, and capacity allocation
- **Cost Insights**: Provides monthly cost estimates and identifies potential savings
- **Volume-Level Analysis**: Detailed metrics for each volume including I/O patterns and efficiency ratios
- **Actionable Recommendations**: Clear, specific suggestions for optimization
- **Serverless Architecture**: Runs on AWS Lambda with a simple web interface

## Architecture

The application consists of two main components:

1. **Backend (AWS Lambda)**: Performs FSx API calls, data analysis, and generates recommendations
2. **Frontend (HTML/JS)**: Simple web interface that displays analysis results

### Technical Stack

- **AWS Lambda**: Handles FSx API calls and data analysis
- **Amazon API Gateway**: Provides HTTP endpoint for the frontend
- **AWS SDK for Python (boto3)**: Interacts with FSx, CloudWatch, and Pricing APIs
- **HTML/CSS/JavaScript**: Client-side rendering of analysis results

## Deployment

### Prerequisites

- AWS CLI configured with appropriate permissions
- Access to create Lambda functions, API Gateway resources, and IAM roles
- Permission to describe FSx filesystems and CloudWatch metrics

### Lambda Function Setup

1. Create a new Lambda function using Python 3.9+ runtime
2. Set the following environment variables:
   - `REGION`: AWS region to analyze (default: eu-west-1)
   - `LOOKBACK_DAYS`: Number of days to analyze (default: 3)
   - `PERIOD`: CloudWatch period in seconds (default: 840)
   - `PCTL`: Percentile for calculations (default: 95)
3. Attach an IAM role with the following permissions:
   - `fsx:Describe*`
   - `cloudwatch:GetMetricStatistics`
   - `pricing:GetProducts`

### API Gateway Configuration

1. Create a new REST API
2. Add a GET method that integrates with your Lambda function
3. Enable CORS
4. Deploy the API to a stage (e.g., "prod")

### Frontend Deployment

1. Host the index.html file in an S3 bucket configured for static website hosting
2. Update the API endpoint URL in the JavaScript code to point to your API Gateway endpoint

## Usage

1. Open the web interface in a browser
2. Click "Run FSx Analysis" button
3. Review the analysis results and recommendations
4. Implement suggested changes to optimize your FSx environment

## Security Considerations

- The Lambda function requires IAM permissions to access FSx and CloudWatch metrics
- Consider implementing additional authentication for the web interface in production environments
- All data is processed within your AWS account; no data is sent to external services

## Development

### Local Testing

To test the Lambda function locally:

```bash
# Install dependencies
pip install boto3

# Run with AWS credentials
python -c "import lambda_function; print(lambda_function.lambda_handler({}, {}))"
```

### Customization

- Modify the `cold_io_threshold` value in the Lambda code to adjust sensitivity for low I/O detection
- Adjust the `lookback_days` environment variable to change the analysis window
- Customize the HTML/CSS to match your organization's branding

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

*Note: This tool is not officially affiliated with or endorsed by Amazon Web Services or NetApp.*