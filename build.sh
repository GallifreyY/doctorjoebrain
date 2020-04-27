rm -rf ./prod
mkdir -p ./prod

rm - rf ./brain/dist/
cd ./brain
npm run build

mv dist ../prod/
cd ..
cd back-end/
cp -r data ../prod/
cp -r src ../prod/
cp -r test ../prod
cp requirements.txt ../prod