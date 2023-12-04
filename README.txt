My project is an application that rolls a die (1-6) for the user. 
The user can chose to roll the die as much as they like 
or end the application. 

github link: https://github.com/ZubairD25/DevopsA4.git

I tried to create an Docker image using the provided sources but eneded up getting this 
error:
 (venv) PS C:\Users\Zubair\PycharmProjects\net2008\DevOpsA4> docker build -t devopsa4 .
[+] Building 0.1s (2/2) FINISHED                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                           0.0s
 => => transferring dockerfile: 2B                                                                                                             0.0s 
 => [internal] load .dockerignore                                                                                                              0.0s 
 => => transferring context: 2B                                                                                                                0.0s 
ERROR: failed to solve: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount166411095/Dockerfile: no such file or directory

