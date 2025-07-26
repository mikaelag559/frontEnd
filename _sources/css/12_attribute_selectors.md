<div style="text-align: justify">

# 12. Attribute Selectors Summary

```{contents}
```

## Working with Different Attribute Selectors and Links

**Definition**: The `attribute` selector allows you to target HTML elements based on their attributes like the `href` or `title` attributes.

```css
a[href] {
    color: blue;
    text-decoration: underline;
}
```

*   **`title` Attribute**: This attribute provides additional information about an element. Here is how you can target links with the `title` attribute:

    ```css
    a[title] {
        font-weight: bold;
        text-decoration: none;
    }
    ```

## Targeting Elements with the `lang` and `data-lang` Attribute

*   **`lang` Attribute**: This attribute is used in HTML to specify the language of the content within an element. You might want to style elements differently based on the language they are written in, especially on a multilingual website.

    ```css
    p[lang="en"] {
        font-style: italic;
    }
    ```

*   **`data-lang` Attribute**: Custom data attributes like the `data-lang` attribute are commonly used to store additional information in elements, such as specifying the language used within a specific section of text. Here is how you can style elements based on the `data-lang` attribute:

    ```css
    div[data-lang="fr"] {
        color: blue;
    }
    ```

## Working with the Attribute Selector, Ordered List Elements and the `type` Attribute

*   **`type` Attribute**: When working with ordered lists in HTML, the `type` attribute allows you to specify the style of numbering used, such as numerical, alphabetical, or Roman numerals.

    ```css
    /*Example targeting uppercase alphabetical numbering*/
    ol[type="A"] {
        color: purple;
        font-weight: bold;
    }

    /*Example targeting lowercase Roman numerals*/
    ol[type="i"] {
        color: green;
    }
    ```


## Special Attribute Selectors in CSS

* **`[attr]` — Presence Selector**: Selects elements that have a specific attribute, regardless of its value.

  ```css
  input[type] {
      border: 1px solid gray;
  }
  ```

* **`[attr="value"]` — Exact Match**: Targets elements where the attribute value matches exactly.

  ```css
  input[type="checkbox"] {
      margin-right: 10px;
  }
  ```

* **`[attr^="value"]` — Starts With**: Selects elements whose attribute value **starts with** the specified string.

  ```css
  span[class^="rate"] {
      color: gold;
  }
  ```

* **`[attr$="value"]` — Ends With**: Selects elements whose attribute value **ends with** the specified string.

  ```css
  a[href$=".pdf"] {
      text-decoration: underline;
  }
  ```

* **`[attr*="value"]` — Contains Substring**: Selects elements whose attribute value **contains** the given substring anywhere.

  ```css
  div[class*="item"] {
      background-color: #f9f9f9;
  }
  ```

* **`[attr~="value"]` — Contains Whole Word**: Targets elements where the attribute value contains a specific **whole word**, separated by spaces (useful with `class`).

  ```css
  button[class~="active"] {
      background-color: green;
  }
  ```

* **`[attr|="value"]` — Language or Hyphenated Prefix Match**: Selects elements whose attribute value matches exactly or starts with the value followed by a hyphen.

  ```css
  p[lang|="en"] {
      font-family: Arial, sans-serif;
  }
  ```


</div>