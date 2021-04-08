#Please run below command 
docker build -t challengeimage .
docker run --name challenge_b challengeimage
docker run -v ${PWD}:/omnilytics challengeimage
