echo "AWS Account: $1"
echo "aws cloudformation describe-stack-events --stack-name consulting-manager-dynamodb  --region sa-east-1 --profile tcc-td-puc-minas-admin"
aws cloudformation describe-stack-events --stack-name consulting-manager-dynamodb  --region sa-east-1 --profile tcc-td-puc-minas-admin
