# Change Log

## [1.0.5] 2022-06-01
### Improvements

- Built with [CoreUI Generator](https://appseed.us/generator/coreui/)
  - Timestamp: `2022-06-01 08:50`

## [1.0.4] 2022-01-16
### Improvements

- Bump Django Codebase to [v2stable.0.1](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Dependencies update (all packages) 
  - Django==4.0.1
- Settings update for Django 4.x
  - `New Parameter`: CSRF_TRUSTED_ORIGINS
    - [Origin header checking isn`t performed in older versions](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins)  

## [1.0.3] 2021-12-03
### Improvements

- Bump UI: CoreUI v4.1.0

## [1.0.2] 2021-10-07
### Improvements

- Bump Django Codebase to [v2.0.4](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Dependencies update (all packages)
  - Use Django==3.2.6 (latest stable version)
- Better Code formatting
- Improved Files organization
- Optimize imports
- Docker Scripts Update 
- Tooling:
  - Gulp SASS compilation script   
  - `Update README` - Recompile SCSS (new section)
- Fixes: 
  - Patch 500 Error when authenticated users access `admin` path (no slash at the end)
  - Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker 

## [1.0.1] 2020-06-08 
### Improvements

- Bump the Core UI Kit to v3.2.0
- Update the code-base to use latest Django Boilerplate - https://github.com/app-generator/boilerplate-code-django-dashboard
- Update Licensing information
- Add CHANGELOG.md to track all changes

## [1.0.0] 2020-01-01
### Initial Release
