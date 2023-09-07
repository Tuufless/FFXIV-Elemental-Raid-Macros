## Folder structure

The files are generally organised as follows:

```
<phase>
  |-- <assets>
  `-- index.en.md
```

This is for the following reasons:

- To make way for multilingual support (e.g: `index.jp.md`).
- Markdown files cannot include images from parent directories, hence all assets need to be in a subdirectory.
- I have decided to split README.md and index.md files to differentiate between notes and content.