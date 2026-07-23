FROM alpine
WORKDIR /myapp
ENV PORT=3000
ENV HOST=localhost
ENV USER=root
ENV PASSWORD=root
ENV DB=vwdb
ENV CONLIMIT=10
COPY . .
RUN apk add --no-cache nodejs npm
RUN npm ci --omit-dev
CMD ["node","index.js"]