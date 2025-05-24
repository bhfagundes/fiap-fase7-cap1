resource "aws_rekognition_collection" "collection" {
  collection_id = var.collection_name
}

resource "aws_iam_role" "rekognition_role" {
  name = "${var.project_name}-rekognition-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "rekognition.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "rekognition_policy" {
  name = "${var.project_name}-rekognition-policy"
  role = aws_iam_role.rekognition_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "rekognition:IndexFaces",
          "rekognition:SearchFaces",
          "rekognition:DetectLabels",
          "rekognition:DetectText",
          "rekognition:DetectModerationLabels"
        ]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}

resource "aws_cloudwatch_log_group" "rekognition_logs" {
  name              = "/aws/rekognition/${var.collection_name}"
  retention_in_days = 30
} 