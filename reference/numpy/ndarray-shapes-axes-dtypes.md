# NP-01 — ndarray, shapes, axes, and dtypes

**Runtime:** NumPy 2.3.5. **Documentation:** NumPy 2.3 release series, accessed October 4, 2026.

[Lesson](../../notebooks/numpy/01-ndarray/lesson.ipynb) · [Worked solutions](../../notebooks/numpy/01-ndarray/solution.ipynb) · [Chapter guide](../../notebooks/numpy/01-ndarray/README.md)

## The mental model

An array combines element storage with metadata defining how coordinates address it and how bytes are interpreted. Axis meanings such as batch, time, or channel are your convention. Write them down before choosing an operation.

| Property | Meaning | Example: shape `(2, 3, 4)`, dtype `float32` |
|---|---|---|
| `shape` | Axis lengths, in order | `(2, 3, 4)` |
| `ndim` | Number of axes | `3` |
| `size` | Product of axis lengths | `24` |
| `dtype` | Element representation | `float32` |
| `itemsize` | Bytes per element slot | `4` |
| `nbytes` | `size * itemsize` | `96` |

`nbytes` excludes object overhead and referenced objects, and does not measure the entire backing allocation of a view. Source: [ndarray attributes](https://numpy.org/doc/2.3/reference/arrays.ndarray.html#array-attributes) and [nbytes](https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.nbytes.html).

## Shapes to recognize immediately

| Shape | Interpretation | Number of elements |
|---|---|---|
| `()` | 0-D array, one scalar value | `1` |
| `(n,)` | Vector; no row/column orientation | `n` |
| `(1, n)` | Row | `n` |
| `(n, 1)` | Column | `n` |
| `(2, 0, 3)` | Three axes, no values | `0` |

`len(a)` is the first axis length, not `size`; it raises `TypeError` for 0-D arrays. A NumPy scalar is not a 0-D ndarray. A vector's `.T` is still one-dimensional. Sources: [shape](https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.shape.html), [scalars](https://numpy.org/doc/2.3/reference/arrays.scalars.html), [transpose](https://numpy.org/doc/2.3/reference/generated/numpy.transpose.html).

## Reconstruct a reduction

For `X` of shape `(B, T, C)`, one mean per channel is

$$\mu_c=\frac{1}{BT}\sum_{b=0}^{B-1}\sum_{t=0}^{T-1}X_{b,t,c}.$$

The surviving index is `c`: reduce `(0, 1)`. The result has shape `(C,)`, or `(1, 1, C)` with `keepdims=True`. `axis=-1` would remove channels instead. Source: [mean](https://numpy.org/doc/2.3/reference/generated/numpy.mean.html).

```python
import numpy as np

x = np.arange(24, dtype=np.int16).reshape((2, 4, 3))
means = x.mean(axis=(0, 1), dtype=np.float64, keepdims=True)
assert means.shape == (1, 1, 3)
assert np.array_equal(means[0, 0], [10.5, 11.5, 12.5])
```

## Reshape is not a permutation

To convert NHWC to NCHW, enforce `out[b, c, h, w] == images[b, h, w, c]`. Use `images.transpose((0, 3, 1, 2))`. A reshape can have the same target shape and still scramble the meaning of elements. Check coordinate values, not just dimensions. Sources: [reshape](https://numpy.org/doc/2.3/reference/generated/numpy.reshape.html), [transpose](https://numpy.org/doc/2.3/reference/generated/numpy.transpose.html).

## Dtype decisions that change correctness

- Check representable integer bounds with `np.iinfo`. Widen **before** arithmetic that could overflow.
- For uint8 image normalization, cast to `float32` before dividing by a floating 255. Avoid integer floor division.
- `astype` defaults to copying and may lose information. Casting finite in-range floats to integers truncates toward zero.
- `float32` cannot distinguish the specific pair `2**24` and `2**24 + 1`. Casting those stored values to float64 does not recover the lost difference.
- `np.finfo(dtype).eps` describes spacing near 1, not an absolute error tolerance at every magnitude.

Sources: [iinfo](https://numpy.org/doc/2.3/reference/generated/numpy.iinfo.html), [astype](https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.astype.html), [finfo](https://numpy.org/doc/2.3/reference/generated/numpy.finfo.html). The precision pair is tested in E08.

## Active recall

1. A `(4, 7, 3)` uint16 array: how many axes, values, and logical bytes?
2. What shape remains after averaging axes `(0, 2)`? What if dimensions are retained?
3. Why does `.T` fail to make a column from a vector?
4. Why might a 16-byte view retain a much larger allocation?
5. Why can output-shape checks miss a broken image-layout conversion?

<details><summary>Check after answering</summary>

1. Three axes, 84 values, 168 bytes.
2. `(7,)`; with `keepdims=True`, `(1, 7, 1)`.
3. One axis has no second axis to exchange with it.
4. The view can reference and keep alive a larger backing array; its logical byte count does not include that full allocation.
5. Reshaping and transposing can agree on shape but disagree on coordinate-to-value correspondence.

</details>

Return to E01–E03 for shape reasoning, E04–E05 for axes, E06–E08 for types, or E09 for integration. The next planned topics are NP-02 creation/conversion, NP-03 type promotion, and NP-05 memory layout.
