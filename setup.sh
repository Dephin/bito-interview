cd vue-bito
npm run build
cd ../
mv vue-bito/dist/static flask-bito/
mv vue-bito/dist/* flask-bito/templates/
cd flask-bito
pip install -r resources/requirements.txt
