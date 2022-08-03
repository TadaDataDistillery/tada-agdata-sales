resource "aws_ecr_repository" "lambda_ecr" {
  name = "${local.project}-lambda-ecr-${var.env}"
}

resource "null_resource" "image_build" {
  depends_on = [aws_ecr_repository.lambda_ecr]
  triggers = {
    image_sha = "image_base_build-${local.image_patch_version}"
  }
  provisioner "local-exec" {
    command = <<EOT
    docker login -u AWS -p $(aws ecr get-login-password --region us-east-1 ) ${local.base_ecr_url}
    echo "############ building Image and tagging with sha ############"
    cd src
    docker build -t ${local.base_ecr_url}:${local.image_data_version} -f Dockerfile .
    echo "############ Tagging Image ############"
    docker tag ${local.base_ecr_url}:${local.image_data_version} ${local.base_ecr_url}:latest
    docker tag ${local.base_ecr_url}:${local.image_data_version} ${local.base_ecr_url}:${var.env}
    echo "############ Pushing Image ############"
    docker push ${local.base_ecr_url}:${local.image_data_version}
    EOT
  }
}