#Ansible

Install Ansible Galaxy Jenkins CI playbook:
https://galaxy.ansible.com/geerlingguy/jenkins/
ansible-galaxy install geerlingguy.jenkins --ignore-certs
ansible-galaxy install geerlingguy.git --ignore-certs
ansible-galaxy install andrewrothstein.scala --ignore-certs
  Caveat: this role depends on andrewrothstein.java-oracle which doesn't work. You'll need to update the following values in /usr/local/etc/ansible/roles/andrewrothstein.java-oracle:
```
  java_oracle_ver:
    patch: 171
    post_patch: b11
    uuid: '512cd62ec5174c3487ac17c61aaa89e8'
    checksums:
      jre:
        'linux-x64': sha256:d489c36c2b1c056f399fcd3893ee5d80da873ab7d5c73980a7b6cd8b87a6f6ba
      jdk:
        'linux-x64': sha256:b6dd2837efaaec4109b36cfbb94a774db100029f98b0d78be68c27bec0275982
```

Installs roles to /usr/local/etc/ansible/roles/

To run playbook on VM:
vagrant up

To debug failing playbook on VM:
vagrant ssh
cd /etc/ansible/ansible-modules/
sudo ansible-playbook -i hosts jenkins.yml
systemctl status -l jenkins

On host open: http://localhost:8888/
To see Jenkins CLI options: http://localhost:8888/cli/
https://jenkins.io/doc/book/managing/cli/

INSTALL PLUGINS: (8888 on host| 8080 on vm)
wget http://localhost:8888/jnlpJars/jenkins-cli.jar

Plugins:
  * antisamy-markup-formatter
  * blueocean
  * conditional-buildstep
  * github-oauth
  * gradle
  * ldap
  * mask-passwords
  * opsgenie
  * rebuild
  * slack
  * ssh-slaves

For each plugin:
```
java -jar jenkins-cli.jar -s http://localhost:8888/ install-plugin $plugin --username admin --password admin
```

Restart Jenkins:
```
java -jar jenkins-cli.jar -s http://localhost:8888/ restart --username admin --password admin
```

CONFIGURE GITHUB AUTHENTICATION:
https://serversforhackers.com/c/github-authentication-authorization

## Getting started
Generate scaffolding for additional roles:
1. cd /etc/ansible
2. sudo clone git@github.com:davestern/ansible-init.git
3. cd config_management/ansible
4. sudo ansible-playbook /etc/ansible/ansible-init/init.yml -i /etc/ansible/ansible-init/production --connection=local --extra-vars='{"roles": ["jenkins"], "project_dir": "/Users/len/estalea/github/config_management/ansible"}'

## Pre-commit hooks for code quality

Install the pre-commit tool and ansible-lint

```shell
pip3 install pre-commit ansible-lint
```

Once those are installed, install the pre-commit hooks for the repository.

```shell
pre-commit install
```

and to test your code before submission, you can run

```shell
pre-commit run --all-files
```

#Terraform
Before pushing terraform changes:
```
terraform fmt
terraform init
terraform validate
```

#GCP
## GCP Project Initialisation Process
[Follow these steps](https://docs.google.com/document/d/1rIQGpJVGFi-dY-X79fy7iFeoXEklPHjen4P4MYLAO0A/edit#)

## Service accounts for Terraform & Packer 
Both tools use service accounts to provision resources on GCP projects.

We'll use Cloud Key Management Service (KMS) to secure the various key files. 
Following [Google's recommendation](https://cloud.google.com/kms/docs/store-secrets), we'll make use of a key ring called _devops_ created in [impact-kms-management](https://console.cloud.google.com/security/kms?organizationId=809907826893&project=impact-kms-management).
It'll be used to encrypt a key file to be stored in GCS in the project where the service account exists. 
The cipher text should be stored in `gs://<project>_secrets`.

**Encrypt**
1. Create key: `https://console.cloud.google.com/iam-admin/serviceaccounts?project=<project>`
2. Encrypt the key: 
```
gcloud kms encrypt --project impact-kms-management \
--location global --keyring devops --key key1 \
--plaintext-file ~/Downloads/<json key file> \
--ciphertext-file <service account name>.json.encrypted
```
3. Upload to GCS bucket: `gsutil cp <service account name>.json.encrypted gs://<project>-secrets`

**Decrypt** 
1. Download ciphertext: `gsutil cp gs://<project>-secrets/<service account name>.json.encrypted .`
2. Decrypt: 
```
gcloud kms decrypt --project impact-kms-management \
--location global --keyring devops --key key1 \
--plaintext-file <service account name>.json \
--ciphertext-file <service account name>.json.encrypted
```

Decrypted key files should be discarded after use.
