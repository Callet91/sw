# tf-ansible-gce-template

A tensorflow template aimed to ease 

## Table of Contents
* [Motivation](#motivation)
* [Prerequisite](#prerequisite)
* [Get started](#get-started)
  * [Create a project](#create-a-project)
  * [Create a service account](#create-a-project)


## Motivation
When students start their first deep-learning course, many face the issue (according to my experience) how they should structure their deep-learning project and how to get it up and running on a GCE instance to train their models. The thing that comes next is how to manage the code on their GCE instance. This repo aims to ease this process by providing a template using  **Ansible** to automatic spin up a **GCE instance** to deploy a **Docker container** running **tensorflow** in **jupyter notebook**.  

## Prerequisite

* Google Cloud Account
  * You can find the information for setting up a Google Cloud Account [here](https://console.cloud.google.com/)
* gcloud SDK
  * Used for managing verifications between Ansible and your cloud-project. For more information, visit [gcloud](https://cloud.google.com/sdk)
  * For installation instructions, please visit [gcloud/install](https://cloud.google.com/sdk/docs/install)
* Ansible
  * Used for automating the GCE instance. For more info visit [Ansible]( https://www.ansible.com/). 
  * For installation instructions, please visit [ansible/install](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

## Get started

### Create a project

To create a project, please follow googles [official instructions](https://cloud.google.com/resource-manager/docs/creating-managing-projects#console).

## Create a service account 

You need a **service account** in order to grant Ansible permissions on your GCP project. To create a service account go to **Navigation Menue -> IAM & Admin -> Service Accounts**. Click the **CREATE SERVICE ACCOUNT** button and follow the steps. **NOTE**: Make sure you select the roles **Compute OS Admin Login**, **Editor** and **Service Account User**. Then click continue and then done. 

Next, create a key under the Action column and download as a .JSON. 

## Grant the ansible access




