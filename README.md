# AWS Infrastructure as Code

![Kube architecture][logo]

[logo]: https://github.com/ramiljoaquin/HelloKubernetes_AKS/blob/master/assets/KubeArchitecture.png 'Kubernetes architecture'

## Course details

54m 5s Intermediate Released: 12/10/2019

Traditionally, working with infrastructure in the cloud requires knowledge of domain-specific languages such as Terraform, network infrastructure, operating systems, and more. AWS Cloud Development Kit (CDK) simplifies this process for developers, allowing them to leverage their existing programming skills to deploy infrastructure. In this course, join Carlos Rivas as he explores a real-world architecture and shows how to write the code to deploy it using AWS CDK and Python. Carlos helps to familiarize you with the basics of working with CDK, as well as how to set it up and create your first CDK project. He then covers how to implement networking, validate your deployed subnets, use the CDK packages for load balancing, verify that everything is up and running in your deployment, and more.

## Learning objectives

- What is the AWS Cloud Development Kit (CDK)?
- Required routing configuration
- Server and load balancer requirements
- Setting up the AWS CDK
- CDK networking
- Validating your deployed subnet
- Autoscaling and server configuration
- Full deployment validation
- Skills covered in this course
- Cloud DevelopmentAmazon Web Services (AWS)

## Instructor

Carlos Rivas
AWS Infrastructure Expert


# What is the AWS Cloud Development Kit?
- [Instructor] Before we dive in, let's take a quick look at what the product is and what it's supposed to do. 

The AWS Cloud Development Kit is a framework used to create infrastructure as code in AWS. It provides you object oriented classes with functionality to support most common cloud related tasks of provision in networks and resources, such as EC2 instances and load balancers. You can do this by levering your existing knowledge of Python, TypeScript, or JavaScript. It works the same regardless of your programming language of choice. 

You can use it to build and deploy the necessary infrastructure that your web application will need to run on. Behind the scenes a cloud formation stack is generated, but you'll never need to maintain the cloud formation code directly. The cloud development kit differs from standard software development kits in that it provides plenty of logic and default values to increase your productivity, and reduce the amount of code required to perform common tasks. 


It allows you to focus on your application and your deployment, and lets you forget about the specific details regarding network and infrastructure. The resulting code is very easy to read and maintain, and is typically very short. In fact, if you come from cloud formation, you can expect a factor of 10 in reduction of lines of code, so expect to write in 20 lines something that would take you about 200 in cloud formation. 

This, in itself, is an amazing productivity boost. Other than productivity, its main feature is that it's an opinionated framework, meaning that it is designed to reduce friction between the tasks at hand and the necessary instructions to achieve it. 

It works the same regardless of your choice of programming language, and it's constantly being expanded which suggests that this is the way AWS wants us to proceed going forward.
