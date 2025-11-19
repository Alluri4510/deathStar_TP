## Implementation Plan
`Team11/raspberryPiCode/main.py` contains the master program that will be going on the Raspberry Pi. Any other code to be run on the Raspberry Pi should go in that directory.
`Team11/serverCode/main.py` contains the master program that will be going on the server computer. Any other code to be run on the server should go in that directory.
Each protocol that manipulates the files or moves them to a new stage should rename them with a new prefix while retaining the original ID 

[**(√)**]() indicates that it works

#### Raspberry Pi `main.py` specifications:

> `string bash(command : string, log_filename : string)`[**(√)**]()<br>
> interprets `command` as a bash command and returns stdout. All output is written to the log file

> `void download_png_files(source_dirname : string, destination_dirname : string, prefix : string)`[**(√)**]()<br>
> downloads all png files from `source_dirname` (assuming this points to a flash drive) and moves and renames them to `destination_dirname`. The naming scheme uses prefixes and IDs, where the prefix is a single character and tracks what stage the image is in, and the ID uniquely identifies the file with an index. This is the first stage where prefixes and IDs are introduced.

>`void preprocess_images(source_dirname : string, destination_dirname : string, prefix : string)`<br>
> manipulates the images in `source_dirname` to prepare them to be interpreted by the classification ML model, such as image resizing and color mapping. The modified images are moved to `destination_dirname`. The new prefix is prepended but the ID is retained.

> `int[] classify_images(source_dirname : string, num_targets : int)`[**√**]()<br>
> runs all the processed images in `source_dirname` through the classification algorithm. The top `num_targets` images are labeled as targets and their indexes are returned.

> `void encrypt_images(source_dirname : string, destination_dirname : string, prefix : string, log_filename : string, enc_key : int256, iv : int16)`[**(√)**]()<br>
> encrypts all images in `source_dirname` and outputs the encrypted values to `destination_dirname` with the same ID. This function uses bash, so all outputs are stored in `log_filename`. The keys are passed in.

> `int128 calculate_md5(source_filename : string, log_filename)`[**(√)**]()<br>
> hashes the file in `source_filename` using md5. Any bash output is stored in the log file.

> `string poll_zigbee(message : string)`<br>
> sends `message` to the server via zigbee and polls the zigbee buffer. Once a message is recieved, the contents of the buffer is returned and cleared.

> `void send_usb_transmission(filename : string)`<br>
> uses the Li-Fi circuit connected to the breakout USB unit to send serial data of the file to the server.

#### Server `main.py` specifications:

> `string bash(command : string, log_filename : string)`[**(√)**]()<br>
> interprets `command` as a bash command and returns stdout. All output is written to the log file

> `string poll_zigbee(hash : string)`<br>
> sends the most recent `hash` of an image to the Raspberry Pi via zigbee and awaits a response with polling. The message it receives afterwards is returned and determines whether the next transmission will be a redo or a new image

> `void read_usb_transmission(buffer : string, destination_filename : string)`<br>
> collects all of the raw image pixel data currently stored in `buffer` and converts it into a png with the name and path in `destination_filename`

> `void crop_images(source_dirname : string, destination_dirname : string, prefix : string)`[**(√)**]()<br>
> runs all the processed images in `source_dirname` through the cropping algorithm and moves them to `destination_dirname` with the new `prefix` applied.

> `void decrypt_images(source_dirname : string, destination_dirname : string, prefix : string, log_filename : string, dec_key : int256, iv : int16)`[**(√)**]()<br>
> decrypts all images in `source_dirname` and outputs the decrypted values to `destination_dirname` with the same ID. This function uses bash, so all outputs are stored in `log_filename`. The keys are passed in.

> `int128 calculate_md5(source_filename : string, log_filename)`[**(√)**]()<br>
> hashes the file in `source_filename` using md5. Any bash output is stored in the log file.

> `png get_image(filename : string)`[**(√)**]()<br>
> serves as an API on the web to request images

## Zigbee Resources

#### Youtube tutorials:
https://www.youtube.com/watch?v=UmpDXc3cXbU<br>
General overview of zigbee protocols

https://www.youtube.com/watch?v=4usy1ESI4k4<br>
https://www.youtube.com/watch?v=4jqQCxjlRDU<br>
How to flash router firmware

#### Sonoff Manuals
https://sonoff.tech/wp-content/uploads/2024/12/User-Manual-ZBDongle-E-V1.2.pdf<br>
https://sonoff.tech/product-review/sonoff-zigbee-3-0-usb-dongle-plus-tutorials/<br>
https://sonoff.tech/product-review/how-to-use-sonoff-dongle-plus-on-home-assistant-how-to-flash-firmware/<br>
https://sonoff.tech/wp-content/uploads/2023/02/SONOFF-Zigbee-3.0-USB-dongle-plus-firmware-flashing.pdf

#### Home Assistant Documentation/Tutorials
https://www.home-assistant.io/integrations/zha<br>
https://www.home-assistant.io/installation/windows<br>
https://developers.home-assistant.io/docs/api/websocket/

#### Firmware Flashing
https://github.com/Koenkk/Z-Stack-firmware/blob/master/router/Z-Stack_3.x.0/bin/CC1352P2_CC2652P_launchpad_router_20221102.zip<br>
https://github.com/itead/Sonoff_Zigbee_Dongle_Firmware/tree/master/Dongle-E/Router<br>
https://www.ti.com/tool/download/FLASH-PROGRAMMER-2/1.8.2<br>
https://www.vandyke.com/cgi-bin/releases.php?product=securecrt

#### Forums
https://e2e.ti.com/support/wireless-connectivity/zigbee-thread-group/zigbee-and-thread/f/zigbee-thread-forum/1059218/sonoff-dongle-cc2562p-doesn-t-enter-in-bootloader-mode<br>
https://e2e.ti.com/support/wireless-connectivity/other-wireless-group/other-wireless/f/other-wireless-technologies-forum/15829/how-to-include-a-pc-into-zigbee-network

