FROM node:20-alpine AS builder

WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM node:20-alpine

WORKDIR /app
RUN adduser -D appuser

COPY --from=builder /app .

USER appuser

HEALTHCHECK CMD wget --spider http://localhost || exit 1

CMD ["npm", "start"]