# Nome da imagem e container
IMAGE_NAME=acmevita-api
CONTAINER_NAME=acmevita-api-container
PORT=8000

# Builda a imagem Docker
build:
	sudo docker build -t $(IMAGE_NAME) .

# Executa o container
run:
	sudo docker run -it --rm -p $(PORT):8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Rebuilda a imagem (remove e builda novamente)
rebuild:
	sudo docker rmi -f $(IMAGE_NAME) || true
	sudo $(MAKE) build

# Executa a aplicação com bind de volume (modo desenvolvimento)
dev:
	sudo docker run -it --rm -p $(PORT):8000 -v $$PWD:/app --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Remove o container e imagem, se existirem
clean:
	sudo docker rm -f $(CONTAINER_NAME) || true
	sudo docker rmi -f $(IMAGE_NAME) || true
