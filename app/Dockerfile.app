FROM node:22-alpine as build-stage

WORKDIR /app

COPY ./app/package*.json ./
RUN npm ci

COPY ./app .
COPY ./app/types/wow.d.ts ./node_modules/@types/wow.d.ts

RUN npm run build

FROM nginx:stable-alpine3.19 as production-stage

COPY --from=build-stage /app/dist  /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]