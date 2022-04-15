# =============================================================================
# Base
# =============================================================================
FROM node:lts-alpine AS base
RUN npm install -g http-server
WORKDIR /app
# ENV PATH /app/node_modules/.bin:$PATH
COPY package*.json ./

# =============================================================================
# Development
# =============================================================================
FROM base AS development
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080
#CMD ["npm", "run", "serve"]
CMD [ "http-server", "dist" ]

# =============================================================================
# Production
# =============================================================================
FROM base AS production
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080
# CMD ["npm", "run", "serve"]
CMD [ "http-server", "dist" ]