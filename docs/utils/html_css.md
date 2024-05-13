# HTML & CSS 一些用过的部件

## Grid

这个 grid 的部件能实现 把页面分成几个网格，然后并排展示

```html title="code"
<div class="grid" style="grid-template-columns: repeat(3, 1fr) !important;" markdown>
<figure markdown="span" style="grid-column-start: 1; grid-column-end: 3;">![](./pics/LSTM_3.webp)</figure>
<p style="grid-column-start: 3; grid-column-end: 4;">展示效果：左图右字，分了3格，左图占2， 右字占1</p>
</div>
```

**展示：**

<div class="grid" style="grid-template-columns: repeat(3, 1fr) !important;" markdown>
<figure markdown="span" style="grid-column-start: 1; grid-column-end: 3;">![]()</figure>
<p style="grid-column-start: 3; grid-column-end: 4;">展示效果：左图右字，分了3格，左图占2， 右字占1</p>
</div>

**可能用到的链接：**

- [grid-template-columns](https://css-tricks.com/almanac/properties/g/grid-template-columns/)
