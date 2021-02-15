# tf-ansible-gcp-template

A tensorflow template aimed to ease the workflow of tensorflow projects on GCP. 

## Table of Contents
* [Motivation](#motivation)
* [Prerequisite](#prerequisite)
* [Getting started](#getting-started)
  * [Create a project](#create-a-project)
  * [Create a service account](#create-a-project)
  * [Grant Ansible access](#grant-ansible-access)
  * [Spin up and start GCP instance](#spin-up-and-start-gcp-instance)
  * [Stop GCP instance](#stop-gcp-instance)
  * [Cleanup GCP instance](#stop-gcp-instance)
 * [Further reading](#further-reading)
  

## Motivation
When students start their first deep-learning course, many face the issue (according to my experience) how they should structure their deep-learning project and how to get it up and running on a GCP instance to train their models. Another issue is also how to manage the code on their GCP instance. This repo aims to ease the workflow by providing a template using  **Ansible** to automatic spin up a **GCP instance** to deploy a **Docker container** running **tensorflow** in **jupyter notebook**.  

## Prerequisite

* Google Cloud Account
  * You can find the information for setting up a Google Cloud Account [here](https://console.cloud.google.com/).
* gcloud SDK
  * Used for managing verifications between Ansible and your cloud-project. For more information, visit [gcloud](https://cloud.google.com/sdk).
  * For installation instructions, please visit [gcloud/install](https://cloud.google.com/sdk/docs/install).
* Ansible
  * Used for automating the GCP instance. For more info visit [Ansible]( https://www.ansible.com/). 
  * For installation instructions, please visit [ansible/install](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

## Getting started

### ATTENTION 
**!!NOTE THAT THESE STEPS WILL CREATE A GCP INSTANCE. BE SURE TO CHECK PRICING AT GOOGLE CLOUD BEFORE STARTING AND REMEMBER TO [STOP YOUR GCP INSTANCE](*stop-gcp-instance) TO PREVENT UNECESSARY COSTS!!**

### Create a project

To create a project, please follow googles [official instructions](https://cloud.google.com/resource-manager/docs/creating-managing-projects#console).

### Create a service account 

You need a **service account** in order to grant Ansible permissions on your GCP project. To create a service account go to **Navigation Menu -> IAM & Admin -> Service Accounts**. Click the **CREATE SERVICE ACCOUNT** button and follow the steps. **NOTE**: Make sure you select the roles **Compute OS Admin Login**, **Editor** and **Service Account User**. Click continue and then done. 

Next, create a **key** under the **Action** column and download as a .JSON. 

### Grant Ansible access

In order to grant permission to access your account, run: 

```sh 
gcloud auth activate-service-account --key-file=/path/to/my/key_file.json
```

Next, add your [ssh-key](https://www.ssh.com/ssh/keygen/) to your service account by running: 

```sh 
gcloud compute os-login ssh-keys add --key-file=.ssh/id_rsa.pub
```

You will get an output similar to this: 

```sh 
loginProfile:
  name: '12346789'
  posixAccounts:
  - accountId: my-project-123
    gid: '12346789132456'
    homeDirectory: /home/sa_123456789
    name: users/name-of-service-account-svc@my-project.iam.gserviceaccount.com/projects/my-project-1234 
    operatingSystemType: LINUX
    primary: true
    uid: 'some uid'
    username: sa_123456789
    .
    .
    .
```
Write down your **username** (here it is "sa_123456789"). 

### Configure variables 
Change the variables in [vars/ansible_vars] to fit your project settings. 

### Spin up and start GCP instance

* Go to the **ansible-scripts** folder and run the following command (this will start an instance configured according to the vars in vars/ansible_vars and install necessary packages): 

```sh 
ansible-playbook spin-up-instance.yaml --user <your_username>
```

* Next, run the following script to copy **src** and the **Dockerfile** into the instance to build the docker image and start up the docker container that runs jupyter. 

```sh 
ansible-playbook start-instance.yaml --user <your_username>
```

When the playbook is done you can go to the prompted ip and use your token (127.0.0.1:8888/?token=**"your-token"**) that is printed to the terminal. This will open up jupyter and you can go to src to test an example model. 

### Stop GCP instance

To stop the GCP instance, simply run the **stop-instance.yaml** playbook. 

```sh 
ansible-playbook stop-instance.yaml 
```

### Cleanup GCP instance

To terminate/delete the GCP instance, run the **cleanup-instance.yaml** playbook. **Note that this will delete the instance permantly.**

```sh 
ansible-playbook cleanup.yaml 
```

## Further reading 
**Ansible** 
* Please visit [Ansible docs](https://docs.ansible.com/ansible/latest/index.html) for more information regarding the ansible scripts.  
* Also check [Cloud Advocates](https://github.com/cloudadvocate/google-cloud) [youtube video](https://www.youtube.com/watch?v=Mt7oKY3gpM8) that have helped a lot during the creation of this repo. 

**GCP**
* Googles [tutorial](https://cloud.google.com/ai-platform/docs/getting-started-tensorflow-estimator) for tensorflow on gcp is a good source for information if you want to expand this repo.

**Tensorflow**
* Check out [Datacamps](https://www.datacamp.com/community/tutorials/tensorflow-tutorial) tutorial on tensorflow to get started with the API. 
* Also check tensorflows [official documentation](https://www.tensorflow.org/api_docs/python/tf) and the [beginners guide](https://www.tensorflow.org/tutorials/quickstart/beginner).









