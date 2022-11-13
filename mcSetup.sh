yum install -q -y java

sudo su
mkdir /opt/minecraft /opt/minecraft/server
cd /opt/minecraft/server

wget https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar

echo '#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).
#$(date)
eula=true
' > eula.txt

java -Xmx512M -Xms512M -jar server.jar nogui