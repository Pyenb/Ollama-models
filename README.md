<h1 align="center">
Ollama model repository 🦙
</h1>

![sync models](https://github.com/Pyenb/Ollama-models/actions/workflows/main.yaml/badge.svg)

This repository fulfills a simple purpose: to provide models for [ollama](https://github.com/ollama/ollama/) to machines that are not connected to the internet.

## Table of contents 📚

- [Getting started](#getting-started-)
- [Download links](#download-links-)
- [Manual export](#manual-export-)
- [FAQ](#faq-)

## Getting started 🚀

1. Download the model you want to use from the [download links](#download-links-) section.
2. Extract the downloaded file `.tar.gz` file. Then extract the `.tar` file located inside the extracted folder.
3. Move the extracted folder `models` to the root of your `.ollama` folder (e.g. `/usr/share/ollama/.ollama/models`). See [where-are-models-stored](https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored), from the official `ollama` FAQ for more information.
4. You should now be able to use the model you downloaded. Executing `ollama run MODEL_NAME` should work as expected, without it trying to download the model.

## Download links 📥

> [!IMPORTANT]
> Due to Contabo limiting my bandwidth to only 100 Mbit/s because my STORAGE VPS is exceeding their set average bandwidth, I’ve added torrents and purchased a Seedbox. Feel free to download and seed them!
>
> With the current setup, downloading the files via the Torrents is the fastest way to get the models.

<!-- MODEL_TABLE_START -->
| Model | Parameters | Last Modified | Size | Download Links |
| --- | --- | --- | --- | --- |
| codellama | 7B | 2024-08-18 16:48 | 3.4G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/codellama:7b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/codellama:7b.tar.gz.torrent) |
| deepseek-coder-v2 | 16B | 2025-01-02 23:18 | 5.2G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/deepseek-coder-v2:16b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/deepseek-coder-v2:16b.tar.gz.torrent) |
| gemma2 | 2B | 2024-08-18 15:45 | 1.5G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/gemma2:2b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/gemma2:2b.tar.gz.torrent) |
| gemma2 | 9B | 2024-08-18 18:24 | 4.8G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/gemma2:9b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/gemma2:9b.tar.gz.torrent) |
| gemma2 | 27B | 2024-08-19 17:23 | 14G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/gemma2:27b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/gemma2:27b.tar.gz.torrent) |
| llama2-uncensored | 7B | 2024-08-18 16:32 | 3.4G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/llama2-uncensored:7b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/llama2-uncensored:7b.tar.gz.torrent) |
| llama3.1 | 8B | 2024-08-19 17:31 | 4.1G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/llama3.1:8b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/llama3.1:8b.tar.gz.torrent) |
| llama3.1 | 70B | 2024-08-18 19:51 | 35G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/llama3.1:70b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/llama3.1:70b.tar.gz.torrent) |
| llama3.2-vision | 11B | 2024-11-13 19:53 | 6.7G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/llama3.2-vision:11b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/llama3.2-vision:11b.tar.gz.torrent) |
| llama3.2 | 1B | 2024-10-07 00:38 | 1.2G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/llama3.2:1b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/llama3.2:1b.tar.gz.torrent) |
| llama3.2 | 3B | 2024-10-07 00:36 | 1.8G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/llama3.2:3b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/llama3.2:3b.tar.gz.torrent) |
| llama3 | 8B | 2024-08-18 20:13 | 4.1G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/llama3:8b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/llama3:8b.tar.gz.torrent) |
| mistral-nemo | 12B | 2024-08-19 15:27 | 6.3G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/mistral-nemo:12b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/mistral-nemo:12b.tar.gz.torrent) |
| mistral | 7B | 2024-08-18 20:08 | 3.6G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/mistral:7b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/mistral:7b.tar.gz.torrent) |
| moondream | 1.8B | 2024-08-18 16:29 | 1.4G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/moondream:1.8b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/moondream:1.8b.tar.gz.torrent) |
| nomic-embed-text | --- | 2025-01-08 21:31 | 241M | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/nomic-embed-text.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/nomic-embed-text.tar.gz.torrent) |
| phi3 | 3.8B | 2024-08-18 16:20 | 1.9G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/phi3:3.8b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/phi3:3.8b.tar.gz.torrent) |
| qwen2.5-coder | 7B | 2024-11-13 20:27 | 4.3G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/qwen2.5-coder:7b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/qwen2.5-coder:7b.tar.gz.torrent) |
| qwen2.5-coder | 14B | 2024-11-13 20:25 | 8.2G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/qwen2.5-coder:14b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/qwen2.5-coder:14b.tar.gz.torrent) |
| qwen | 0.5B | 2024-08-19 14:48 | 356M | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/qwen:0.5b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/qwen:0.5b.tar.gz.torrent) |
| qwen | 32B | 2024-08-19 15:01 | 16G | [Storage VPS](https://data.pyenb.network/Github/Ollama/models/qwen:32b.tar.gz) / [Torrent](https://data.pyenb.network/Github/Ollama/models/torrents/qwen:32b.tar.gz.torrent) |
<!-- MODEL_TABLE_END -->

> [!NOTE]
>  [I want a model that is not listed here, what can I do?](#i-want-a-model-that-is-not-listed-here-what-can-i-do)

## Manual export 📦

To export the model yourself, you can use the [ollama-exporter.sh](./ollama-exporter.sh) script, that I created. The script will create a `.tar.gz` file of the model you want to export.

> [!CAUTION]
> This script will delete everything in the `models` folder to make sure that only the model you want to export is present. Make sure to back up any models you want to keep! I did this on a separate VM.

```bash
Usage: ollama-exporter.sh [OPTIONS]

Options:
  -m, --model-name    Name of the model to pull and backup (e.g. "moondream", "gemma2:2b", "llama3.1:70b").
  -d, --dest-folder   Path to the destination folder where the tar.gz file will be moved.
  -f, --model-folder  Path to the ollama model folder (default: /usr/share/ollama/.ollama/models).
  --no-delete         Do not delete the original model folder contents after moving.
  -h, --help          Display this help message and exit.

If no options are provided, the script will display this help message.

Examples:
  ollama-exporter.sh -m moondream -d /path/to/backup -f /custom/path/to/models
  ollama-exporter.sh -m llama3.1:70b -d /home/pyenb/Daten/Backups/Ollama/models
```

###### This script is currently WIP and Linux only. Requires `ollama, rclone, pv and pigz` to be installed

As the model name, everything out of [Ollamas registry](https://registry.ollama.com/library) should work. Everything else should be self-explanatory.

The finished `.tar.gz` file structure will look like this:

```plaintext
MODEL_NAME.tar.gz
└── MODEL_NAME.tar
    └── models
        ├── blobs
        │   └── sha256-...
        └── manifests
            └── registry.ollama.ai
                └── library
                    └── MODEL_NAME
                        └── latest
```

<details>
<summary>Example output</summary>

```bash
pyenb@ollama:~$ sudo ./ollama-exporter.sh -m llama3.1:70b -d /home/pyenb/Daten/Backups/Ollama/models
Pulling the Ollama model: llama3.1:70b...
pulling manifest 
pulling a677b4a4b70c... 100% 39 GB                         
pulling 11ce4ee3e170... 100% 1.7 KB                         
pulling 0ba8f0e314b4... 100% 12 KB                         
pulling 56bb8bd477a5... 100% 96 B                         
pulling 654440dac7f3... 100% 486 B                         
verifying sha256 digest 
writing manifest 
removing any unused layers 
success 
Compressing the model folder...
37.2GiB 0:02:41 [ 235MiB/s] [==========================================================================] 100%            
Moving the tar.gz file to the destination folder using rclone...
2024/08/18 19:51:15 NOTICE: Config file "/root/.config/rclone/rclone.conf" not found - using defaults
Transferred:       35.464 GiB / 35.464 GiB, 100%, 1.243 MiB/s, ETA 0s
Checks:                 2 / 2, 100%
Deleted:                1 (files), 0 (dirs)
Renamed:                1
Transferred:            1 / 1, 100%
Elapsed time:      7m36.3s
Press Enter to continue with deletion or Ctrl+C to cancel...
Deleting the original model folder contents...
Model moved and cleaned up successfully.
```

</details>

## FAQ ❓

### Why not upload them using Github LFS?

With GitHub LFS, a "data pack" costs approximately €5 per month for 50GB of storage. The Storage-VPS I'm using also costs around 5€ per month, but with 800GB of SSD storage. So I decided to host the files myself. The only downside is mostly the download speed, so consider [supporting me](https://github.com/sponsors/Pyenb), so that I can upgrade the server.

### I want a model that is not listed here, what can I do?

You can either create the model yourself by following the [manual export](#manual-export) instructions, or you can open an issue, and I will try to get it done as soon as possible.

## Resources 🔗

- [where-are-models-stored](https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Disclaimer

This repository is for research purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.
