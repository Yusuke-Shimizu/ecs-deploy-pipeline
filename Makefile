test:
	cdk diff
	pytest

install:
	sudo yum -y install epel-release
	sudo yum -y install jq
	pip install --upgrade pip
	pip install -r requirements.txt

set_profile:
	grep CDK ~/.bash_profile
	echo export CDK_DEFAULT_ACCOUNT=`aws sts get-caller-identity | jq --raw-output .Account` >> /home/ec2-user//.bash_profile
	echo export CDK_DEFAULT_REGION=`curl -s http://169.254.169.254/latest/meta-data/local-hostname | cut -d '.' -f2` >> /home/ec2-user//.bash_profile

clean:
	du -sh /tmp/
	rm -rf /tmp/jsii-kernel-* 
	rm -rf /tmp/cdk.out*
	du -sh /tmp/
