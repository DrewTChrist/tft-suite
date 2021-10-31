# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

### Changed

### Removed

## [0.3.0](https://github.com/drewtchrist/tft-suite/releases/tag/v0.3.0) - 2021-10-31
### Added
* 240x240 support
* Typed the project

### Changed
* Disabling the backlight now stops the screenthread to save those precious cycles

### Removed

## [0.2.0](https://github.com/drewtchrist/tft-suite/releases/tag/v0.2.0) - 2021-10-16
### Added
* Added an abstract method `draw_screen` to the `Screen` class

### Changed
* The `run` method of the `Screen` class is no longer abstract and calls the `draw_screen` method

### Removed

