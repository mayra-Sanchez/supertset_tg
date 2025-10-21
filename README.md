APACHE DRILL

Para la instalación de Apache Drill en docker:

docker run -d --name drill -p 8047:8047 apache/drill tail -f /dev/null

Ajuste en Drill para el mongo activado


{
  "type": "mongo",
  "connection": "mongodb://apiUser:userPassword123@mongo-db-registers:27017/epilepsyRegister?authSource=admin",
  "pluginOptimizations": {
    "supportsProjectPushdown": true,
    "supportsFilterPushdown": true,
    "supportsAggregatePushdown": true,
    "supportsSortPushdown": true,
    "supportsUnionPushdown": true,
    "supportsLimitPushdown": true
  },
  "batchSize": 100,
  "enabled": true,
  "authMode": "SHARED_USER"
}


Conectarlas a la misma red

PS C:\Users\mayra\OneDrive\Escritorio> docker network create my-network

PS C:\Users\mayra\OneDrive\Escritorio> docker network ls
NETWORK ID     NAME                   DRIVER    SCOPE
f14bbca6d6a6   bridge                 bridge    local
7d16ec31b529   drill_network          bridge    local
293dd8b9c548   host                   host      local
0e3dd2be54f9   my-network             bridge    local
592caa2c01bb   none                   null      local
6cb0c9644d8a   registersapi_default   bridge    local

PS C:\Users\mayra\OneDrive\Escritorio> docker network connect my-network mongo-db-registers

PS C:\Users\mayra\OneDrive\Escritorio> docker network disconnect bridge drill

PS C:\Users\mayra\OneDrive\Escritorio> docker network connect my-network drill

PS C:\Users\mayra\OneDrive\Escritorio> docker network inspect my-network

Conectar superset a my-network

docker network disconnect superset_my-network superset
docker network connect my-network superset

La siguiente es la URI de superset para Drill, la conexión debería ser exitosa

drill+sadrill://drill:8047/epilepsyRegister?use_ssl=False

