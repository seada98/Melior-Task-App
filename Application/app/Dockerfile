FROM node:20.1.0-alpine

WORKDIR /app
COPY package.json .

RUN apk update
RUN npm install

COPY . .
EXPOSE 3000
CMD ["npm", "start"]