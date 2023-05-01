for path in /data/Twitter\ dataset/geoTwitter20-*.zip; do
    ./src/map.py --input_path="$path"
done
