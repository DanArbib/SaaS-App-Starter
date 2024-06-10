FROM node:14 as build-stage

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build


FROM node:14 as production-stage

WORKDIR /app

COPY --from=build-stage /app/dist /app/dist
COPY server.js .
RUN npm install express

EXPOSE 8080

CMD ["node", "server.js"]