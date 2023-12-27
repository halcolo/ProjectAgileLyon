# Project Poker planning

This project is a Web created to implement a Poker planning in web
Using Python we implemented a Poker Planning, 


## Game modes

### Majority


### Average


### Median

## Generate docs 

Run following command before upload project

```
pydoctor \
    --project-name=poker-planning \
    --project-version=1.0.0 \
    --project-url=https://github.com/jdalfons/ProjectAgileLyon/ \
    --html-viewsource-base=https://github.com/jdalfons/ProjectAgileLyon/tree/main \
    --make-html \
    --html-output=docs/ \
    --project-base-dir="." \
    --docformat=epytext \
    --intersphinx=https://docs.python.org/3/objects.inv \
    ./package ./tools ./api_routes
```