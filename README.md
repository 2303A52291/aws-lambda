# AWS Lambda S3 Alert Function

This project contains an AWS Lambda function (Python) that is triggered by S3 object creation events and sends alerts via SNS.

## Project Structure
- `lambda_function.py`: Lambda function code
- `template.yaml`: AWS SAM/CloudFormation template
  

## Prerequisites
- AWS CLI configured
- AWS SAM CLI installed
- Python 3.12
- **No prior AWS experience required—just follow the steps below!**

## Setup & Deployment (Anyone Can Execute)

1. **Install dependencies** (if any):
   ```powershell
   # No external dependencies required for this example
   ```

2. **Build the SAM application:**
   ```powershell
   sam build
   ```

3. **Deploy the SAM application:**
   ```powershell
   sam deploy --guided
   ```
   - Follow the prompts to set stack name, AWS region, and confirm changes.
   - Set the `your-source-bucket-name` and `youremail@example.com` in `template.yaml` as needed.

4. **Confirm SNS Subscription:**
   - Check your email and confirm the SNS subscription to receive alerts.

5. **Test:**
   - Upload a file to the specified S3 bucket. You should receive an alert via SNS.

## Notes
- The Lambda function reads the SNS topic ARN from the environment variable `ALERT_TOPIC_ARN`.
- Update the `template.yaml` to match your bucket and email.
- **This project is designed so anyone can follow the instructions and execute it successfully, even without prior AWS experience.**

## Cleanup
To delete the stack and all resources:
```powershell
sam delete
```
