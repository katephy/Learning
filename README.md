# Learning

This is a leanring board of me.

## 1. Videos

### 1.1 Front
#### 1.1.1 React
<!-- REACT -->
- [ ] [React](https://github.com/Yin-FR/Learning/blob/main/learnings/React.md) 699/2429 minutes

#### 1.1.2 TypeScript
<!-- TYPESCRIPT -->
- [ ] [TypeScript](https://github.com/Yin-FR/Learning/blob/main/learnings/TypeScript.md) 267/625 minutes


### 1.2 Back
#### 1.2.1 SSM(Spring + Spring MVC + MyBatis)
<!-- SSM -->
- [ ] [SSM](https://github.com/Yin-FR/Learning/blob/main/learnings/SSM.md) 0/2053 minutes

#### 1.2.2 Design Pattern
<!-- DESIGNPATTERN -->
- [ ] [Design Pattern](https://github.com/Yin-FR/Learning/blob/main/learnings/Design%20Pattern.md) 0/1237 minutes


### 1.3 Project
#### 1.3.1 Gulimall
<!-- GULIMALL -->
- [ ] [Gulimall](https://github.com/Yin-FR/Learning/blob/main/learnings/Gulimall.md) 0/6285 minutes

-----
## How to use
*Until now this tool only supplies Bilibili videos*

1. Install package and dependencies
```
git clone https://github.com/Yin-FR/Learning.git
pip install -r requirements.txt
```
2. Modify `basic.md` to customize your main report and define the labels where the generated text will be inserted (the line below label)
3. Write your learning records into `data.json` with this model:
```json
{
  "$LABEL": {
    "title": "$TITLE",
    "bvid": "$BVID",
    "paged": "$IS_PAGED",
    "finished": "$FINISHED_PAGES"
  },
  ...
}
```
4. Run
```
python main.py
```