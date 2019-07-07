cd vue-bito
npm run build
cd ../
rm -rf flask-bito/templates/*
rm -rf flask-bito/static/
mv vue-bito/dist/static flask-bito/
mv vue-bito/dist/* flask-bito/templates/
