package org.broadinstitute.k3.methods

import org.broadinstitute.k3.variant._

abstract class VariantMethod[+T] {
  def name: String
  def apply(vds: VariantDataset): Map[Variant, T]
}