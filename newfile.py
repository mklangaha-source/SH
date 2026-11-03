name: Build APK
on: [push, workflow_dispatch]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install buildozer cython==0.29.33

      - name: Build with Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        with:
          command: buildozer android debug
          buildozer_version: stable

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: SH-APK
          path: bin/*.apk