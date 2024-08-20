# kinopoisk_django

**kinopoisk is a web application that automatically downloads Movies and TV Shows.**

[![Build Status](https://github.com/lardbit/nefarious/actions/workflows/build.yml/badge.svg)](https://github.com/lardbit/nefarious/actions/workflows/build.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/lardbit/nefarious.svg?maxAge=60&style=flat-square)](https://hub.docker.com/r/lardbit/nefarious)

It uses [Jackett](https://github.com/Jackett/Jackett/) and [Transmission](https://transmissionbt.com/) under the hood.  Jackett searches for torrents and Transmission handles the downloading.

Features:
- [x] Search and discover TV & Movies (by popularity, genres, year etc.)
- [x] Auto download TV & Movies
- [x] Find similar and recommended TV & Movies (via The Movie Database & Rotten Tomatoes)
- [x] Manually search and download Jackett's torrent results
- [x] Supports blacklisting torrent results (i.e. permanently avoid a bad/fake torrent)
- [X] Supports quality profiles (i.e. only download *1080p* Movies and *720p* TV)
- [x] Supports whether to download media with hardcoded subtitles or not
- [x] Supports user defined keywords to filter results (i.e. ignore "x265", "hevc" codecs)
- [x] Monitor transmission results & status from within the app
- [x] Self/auto updating application, so you're always up-to-date
- [x] Supports multiple users and permission groups (i.e. admin users and regular users)
- [x] Responsive Design (looks great on desktops, tablets and small devices like phones)
- [x] Includes movie trailers
- [x] Automatically renames media
- [x] Supports multiple languages (TMDB supports internationalized Titles, Descriptions and Poster artwork)
- [x] Notifications - supports all major notification services (via [Apprise](https://github.com/caronc/apprise/tree/v0.9.3))
- [x] Imports existing libraries
- [x] VPN integration (optional)
- [x] Auto download subtitles via [opensubtitles](https://www.opensubtitles.com/) [api](https://opensubtitles.stoplight.io/)
- [x] Autodetect & blacklist [spam/fake](https://github.com/lardbit/nefarious/pull/180) video content
- [x] Autodetect & blacklist "stuck" torrents that fail to complete after X days

### Contents

- [Demo](#demo)
- [Screenshots](#screenshots)
- [Dependencies](#dependencies)
- [Setup](#setup)
- [Usage](#usage)
- [Upgrading](#upgrading)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
