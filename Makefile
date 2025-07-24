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

# Rebuilda a imagem
rebuild:
	sudo docker rmi -f $(IMAGE_NAME) || true
	$(MAKE) build

# Remove o container e imagem, se existirem
clean:
	sudo docker rm -f $(CONTAINER_NAME) || true
	sudo docker rmi -f $(IMAGE_NAME) || true
